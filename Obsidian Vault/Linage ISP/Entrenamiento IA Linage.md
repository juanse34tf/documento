do reiniciaste el router?"
soluciones:
  paso_1:
    accion: "Reiniciar router"
    instruccion: "Desconecta el router 30 segundos y vuelve a conectar"
    tiempo_espera: "2 minutos"
  paso_2:
    accion: "Optimizar WiFi"
    instruccion: "Cambia el canal WiFi a 1, 6 u 11 en 2.4GHz"
  paso_3:
    accion: "Verificar cables"
    instruccion: "Revisa que el cable de fibra no esté doblado"
  escalamiento:
    condicion: "Si persiste después de 3 pasos"
    accion: "Agendar visita técnica"

problema: "Sin conexión"
diagnostico:
  - luces_router: "¿Qué luces ves en el router?"
  - corte_luz: "¿Hubo corte de luz recientemente?"
  - otros_servicios: "¿Los vecinos tienen internet?"
soluciones:
  luz_roja:
    significado: "Problema en fibra óptica"
    accion: "Verificar cable de fibra no esté desconectado"
  sin_luces:
    significado: "Sin energía"
    accion: "Verificar conexión eléctrica y adaptador"
  luz_naranja:
    significado: "Autenticación"
    accion: "Reiniciar y esperar 5 minutos"

problema: "WiFi no aparece"
soluciones:
  - verificar_boton_wifi: "Algunos routers tienen botón físico WiFi"
  - reset_fabrica: "Mantén presionado reset 10 segundos"
  - cambiar_nombre: "El WiFi podría tener otro nombre"
```

---

## 3️⃣ IMPLEMENTACIÓN EN FIREBASE GENKIT

### Configuración del Modelo
```kotlin
// app/src/main/java/com/linage/ai/LinageAIConfig.kt

import com.google.firebase.genkit.*
import kotlinx.coroutines.flow.Flow

class LinageAIAssistant {
    
    private val genkit = Genkit.Builder()
        .addPlugin(firebase())
        .addPlugin(googleAI())
        .build()
    
    private val model = genkit.model("gemini-1.5-pro") {
        config {
            temperature = 0.7  // Balance entre creatividad y precisión
            topK = 40
            topP = 0.95
            maxOutputTokens = 500  // Respuestas concisas
            
            systemInstruction = """
                $SYSTEM_PROMPT
                
                CONTEXTO ADICIONAL:
                - Fecha actual: ${getCurrentDate()}
                - Promociones activas: ${getActivePromotions()}
                - Estado red: ${getNetworkStatus()}
            """
        }
    }
    
    suspend fun processQuery(
        query: String,
        userId: String,
        context: ChatContext
    ): AIResponse {
        
        // Enriquecer contexto
        val enrichedPrompt = buildPrompt(query, userId, context)
        
        // Generar respuesta
        val response = model.generate(enrichedPrompt)
        
        // Post-procesar
        return postProcess(response, context)
    }
    
    private fun buildPrompt(
        query: String, 
        userId: String,
        context: ChatContext
    ): String {
        return """
            CONTEXTO CLIENTE:
            - ID: $userId
            - Plan actual: ${context.currentPlan}
            - Zona: ${context.location}
            - Historial: ${context.lastIssues.takeLast(3)}
            - Estado cuenta: ${context.accountStatus}
            
            CONSULTA: $query
            
            INSTRUCCIONES:
            1. Responde como Lina de Linage ISP
            2. Si es problema técnico, guía paso a paso
            3. Si es comercial, sugiere plan adecuado
            4. Mantén tono amigable pero profesional
            5. Máximo 3 párrafos
        """
    }
}
```

### Manejo de Contexto y Estado
```kotlin
// app/src/main/java/com/linage/ai/ChatContext.kt

data class ChatContext(
    val userId: String,
    val sessionId: String,
    val currentPlan: PlanInfo?,
    val location: Location,
    val accountStatus: AccountStatus,
    val lastIssues: List<Issue>,
    val conversationHistory: List<Message>
) {
    fun toMap(): Map<String, Any> = mapOf(
        "plan" to (currentPlan?.name ?: "Sin plan"),
        "velocidad" to (currentPlan?.speed ?: "N/A"),
        "zona" to location.neighborhood,
        "estado_cuenta" to accountStatus.status,
        "saldo" to accountStatus.balance,
        "ultimo_pago" to accountStatus.lastPayment,
        "tickets_abiertos" to lastIssues.count { it.status == "OPEN" }
    )
}

data class AIResponse(
    val message: String,
    val confidence: Float,
    val suggestedActions: List<Action>,
    val requiresHumanReview: Boolean,
    val metadata: ResponseMetadata
)
```

---

## 4️⃣ BIBLIOTECA DE PROMPTS ESPECIALIZADOS

### Por Tipo de Cliente
```kotlin
object PromptTemplates {
    
    // Cliente Residencial
    val RESIDENTIAL = """
        Contexto: Cliente residencial, enfoque en familia y entretenimiento
        Prioridades: Estabilidad, precio accesible, instalación rápida
        Lenguaje: Simple, evitar tecnicismos
        Ejemplos relevantes: Netflix, videollamadas familia, trabajo desde casa
    """
    
    // Cliente Gamer
    val GAMER = """
        Contexto: Gamer competitivo, sensible a latencia
        Prioridades: Ping bajo (<20ms), NAT abierto, sin packet loss
        Lenguaje: Técnico OK, usar jerga gaming
        Mencionar: Servidores Miami (40ms), Brasil (55ms), sin throttling
        Ejemplos: "GG", "lag", "FPS", "ranked"
    """
    
    // Cliente Empresarial
    val BUSINESS = """
        Contexto: Empresa, requiere confiabilidad
        Prioridades: SLA, uptime 99.9%, IP fija, soporte 24/7
        Lenguaje: Formal, profesional, técnico cuando sea necesario
        Enfoque: ROI, productividad, respaldo
    """
    
    // Cliente Técnico
    val TECHNICAL = """
        Contexto: Usuario avanzado, entiende networking
        Prioridades: Configuración avanzada, IPv6, VLAN, QoS
        Lenguaje: Técnico completo OK
        Puede mencionar: BGP, MTU, jitter, traceroute
    """
}
```

### Respuestas Dinámicas por Escenario
```kotlin
class ResponseGenerator {
    
    fun generateTechnicalSupport(issue: String): String {
        return when {
            issue.contains("lento") -> Templates.SLOW_INTERNET
            issue.contains("no funciona") -> Templates.NO_CONNECTION
            issue.contains("intermitente") -> Templates.INTERMITTENT
            issue.contains("wifi") -> Templates.WIFI_ISSUES
            else -> Templates.GENERIC_SUPPORT
        }
    }
    
    object Templates {
        const val SLOW_INTERNET = """
            Entiendo tu frustración con la velocidad 🔧 
            
            Hagamos un diagnóstico rápido:
            1. **Test de velocidad**: Entra a fast.com desde el dispositivo afectado
            2. **Dispositivos conectados**: ¿Cuántos están usando internet ahora?
            3. **Ubicación**: ¿Estás cerca o lejos del router?
            
            Mientras respondes, voy preparando la solución específica para tu caso.
        """
        
        const val NO_CONNECTION = """
            Veo que estás sin conexión. Vamos a resolverlo rápidamente 🚀
            
            **Verificación rápida del router:**
            - 🟢 Luz verde = Conexión OK
            - 🔴 Luz roja = Problema de fibra
            - ⚫ Sin luz = Sin energía
            
            ¿Qué luces ves en tu router Linage?
        """
    }
}
```

---

## 5️⃣ SISTEMA DE APRENDIZAJE CONTINUO

### Recolección de Feedback
```kotlin
class FeedbackCollector {
    
    fun collectFeedback(
        conversation: Conversation,
        rating: Int,
        resolved: Boolean
    ) {
        val feedback = Feedback(
            conversationId = conversation.id,
            rating = rating,
            resolved = resolved,
            timestamp = System.currentTimeMillis(),
            queryType = classifyQuery(conversation),
            responseTime = conversation.avgResponseTime,
            escalated = conversation.wasEscalated
        )
        
        // Guardar para análisis
        FirebaseFirestore.getInstance()
            .collection("ai_feedback")
            .add(feedback)
        
        // Si fue mal, aprender
        if (rating < 3 || !resolved) {
            scheduleForReview(conversation)
        }
        
        // Si fue excelente, usar como ejemplo
        if (rating == 5 && resolved) {
            addToGoodExamples(conversation)
        }
    }
    
    private fun scheduleForReview(conversation: Conversation) {
        // Marcar para revisión humana
        conversation.metadata["needs_review"] = true
        conversation.metadata["review_reason"] = when {
            conversation.rating < 3 -> "Low rating"
            !conversation.resolved -> "Unresolved"
            conversation.responseTime > 5000 -> "Slow response"
            else -> "Other"
        }
    }
}
```

### Métricas y KPIs
```kotlin
class AIMetrics {
    
    fun calculateMetrics(): MetricsReport {
        return MetricsReport(
            resolutionRate = calculateResolutionRate(),
            avgResponseTime = calculateAvgResponseTime(),
            satisfactionScore = calculateSatisfaction(),
            escalationRate = calculateEscalationRate(),
            topIssues = getTopIssues(),
            performanceByHour = getHourlyPerformance()
        )
    }
    
    data class MetricsReport(
        val resolutionRate: Float,      // Meta: >75%
        val avgResponseTime: Long,       // Meta: <2000ms
        val satisfactionScore: Float,    // Meta: >4.5/5
        val escalationRate: Float,       // Meta: <20%
        val topIssues: List<IssueType>,
        val performanceByHour: Map<Int, Performance>
    )
    
    fun generateDashboard(): Dashboard {
        return Dashboard {
            metric("Resolución sin agente") {
                value = "${resolutionRate}%"
                target = 75
                status = if (resolutionRate > 75) "🟢" else "🔴"
            }
            
            metric("Tiempo respuesta") {
                value = "${avgResponseTime}ms"
                target = 2000
                status = if (avgResponseTime < 2000) "🟢" else "🟡"
            }
            
            metric("Satisfacción") {
                value = "$satisfactionScore/5"
                target = 4.5
                status = if (satisfactionScore > 4.5) "🟢" else "🟡"
            }
        }
    }
}
```

---

## 6️⃣ CASOS DE USO ESPECÍFICOS

### Manejo de Emergencias
```kotlin
class EmergencyHandler {
    
    fun handleEmergency(type: EmergencyType): Response {
        return when (type) {
            EmergencyType.MASSIVE_OUTAGE -> {
                Response(
                    message = """
                        ⚠️ Detectamos una interrupción en tu zona.
                        
                        **Estado**: Nuestro equipo técnico ya está trabajando
                        **Tiempo estimado**: 2-3 horas
                        **Afectados**: Sector ${getAffectedSector()}
                        
                        Te notificaremos por SMS cuando se restablezca.
                        ¿Necesitas internet urgente? Tenemos WiFi gratis en nuestras oficinas.
                    """,
                    priority = Priority.HIGH,
                    autoNotify = true
                )
            }
            
            EmergencyType.FIBER_CUT -> {
                Response(
                    message = """
                        🚧 Corte de fibra detectado en tu sector.
                        
                        Técnicos en camino. ETA: 45 minutos.
                        Mientras tanto, activa datos móviles.
                        
                        Como compensación, recibirás 2 días gratis.
                    """,
                    compensation = true
                )
            }
        }
    }
}
```

### Ventas Inteligentes
```kotlin
class SmartSales {
    
    fun recommendPlan(context: UserContext): PlanRecommendation {
        val usage = analyzeUsage(context)
        
        return when {
            usage.isGamer -> recommendGamerPlan(usage)
            usage.isRemoteWorker -> recommendWorkPlan(usage)
            usage.isFamily -> recommendFamilyPlan(usage)
            usage.isBasic -> recommendBasicPlan(usage)
            else -> recommendStandardPlan(usage)
        }
    }
    
    private fun recommendGamerPlan(usage: Usage): PlanRecommendation {
        return PlanRecommendation(
            plan = "Premium 300 Mbps",
            reason = """
                🎮 Perfecto para gaming:
                - Ping <15ms a servidores Miami
                - 0% packet loss garantizado
                - NAT tipo abierto incluido
                - Prioridad QoS para consolas
            """,
            monthlyPrice = "$99.900",
            savings = "$20.100/mes en promo",
            cta = "¡Instálalo mañana mismo!"
        )
    }
}
```

---

## 7️⃣ INTEGRACIÓN CON LA UI

### Chat Component
```kotlin
@Composable
fun AIChat(
    viewModel: ChatViewModel = hiltViewModel()
) {
    val messages by viewModel.messages.collectAsState()
    val isTyping by viewModel.isTyping.collectAsState()
    
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(LinageTheme.colors.background)
    ) {
        // Header
        ChatHeader(
            title = "Lina - Asistente Linage",
            status = if (isTyping) "escribiendo..." else "en línea",
            onBack = { /* navigate back */ }
        )
        
        // Messages
        LazyColumn(
            modifier = Modifier.weight(1f),
            reverseLayout = true
        ) {
            items(messages.reversed()) { message ->
                ChatBubble(
                    message = message,
                    isFromAI = message.sender == Sender.AI
                )
                
                // Quick actions después de mensaje IA
                if (message.sender == Sender.AI && message.actions.isNotEmpty()) {
                    QuickActions(
                        actions = message.actions,
                        onActionClick = viewModel::executeAction
                    )
                }
            }
            
            // Typing indicator
            if (isTyping) {
                item {
                    TypingIndicator()
                }
            }
        }
        
        // Input
        ChatInput(
            onSendMessage = viewModel::sendMessage,
            suggestions = viewModel.suggestions
        )
    }
}
```

### ViewModel Integration
```kotlin
@HiltViewModel
class ChatViewModel @Inject constructor(
    private val aiAssistant: LinageAIAssistant,
    private val userRepository: UserRepository,
    private val analyticsLogger: AnalyticsLogger
) : ViewModel() {
    
    private val _messages = MutableStateFlow<List<ChatMessage>>(emptyList())
    val messages = _messages.asStateFlow()
    
    private val _isTyping = MutableStateFlow(false)
    val isTyping = _isTyping.asStateFlow()
    
    fun sendMessage(text: String) {
        viewModelScope.launch {
            // Add user message
            _messages.value += ChatMessage(
                text = text,
                sender = Sender.USER,
                timestamp = System.currentTimeMillis()
            )
            
            // Show typing
            _isTyping.value = true
            
            try {
                // Get AI response
                val context = buildContext()
                val response = aiAssistant.processQuery(
                    query = text,
                    userId = userRepository.currentUserId,
                    context = context
                )
                
                // Add AI message with streaming effect
                streamResponse(response.message)
                
                // Log analytics
                analyticsLogger.logAIInteraction(
                    query = text,
                    response = response,
                    responseTime = response.metadata.processingTime
                )
                
            } catch (e: Exception) {
                handleError(e)
            } finally {
                _isTyping.value = false
            }
        }
    }
    
    private suspend fun streamResponse(text: String) {
        val words = text.split(" ")
        var currentText = ""
        
        words.forEach { word ->
            currentText += "$word "
            _messages.value = _messages.value.dropLast(1) + 
                ChatMessage(
                    text = currentText.trim(),
                    sender = Sender.AI,
                    timestamp = System.currentTimeMillis()
                )
            delay(50) // Efecto de escritura
        }
    }
}
```

---

## 8️⃣ MONITOREO Y MEJORA CONTINUA

### Dashboard de Métricas
```kotlin
@Composable
fun AIMetricsDashboard(
    metrics: AIMetrics.MetricsReport
) {
    LazyVerticalGrid(
        columns = GridCells.Fixed(2),
        contentPadding = PaddingValues(16.dp)
    ) {
        item {
            MetricCard(
                title = "Resolución IA",
                value = "${metrics.resolutionRate}%",
                target = "Meta: 75%",
                color = if (metrics.resolutionRate > 75) Green else Red
            )
        }
        
        item {
            MetricCard(
                title = "Tiempo Respuesta",
                value = "${metrics.avgResponseTime}ms",
                target = "Meta: <2000ms",
                color = if (metrics.avgResponseTime < 2000) Green else Yellow
            )
        }
        
        item {
            MetricCard(
                title = "Satisfacción",
                value = "${metrics.satisfactionScore}/5",
                target = "Meta: 4.5/5",
                color = if (metrics.satisfactionScore > 4.5) Green else Yellow
            )
        }
        
        item {
            MetricCard(
                title = "Escalamiento",
                value = "${metrics.escalationRate}%",
                target = "Meta: <20%",
                color = if (metrics.escalationRate < 20) Green else Red
            )
        }
    }
}
```

---

## 🚀 DEPLOYMENT CHECKLIST

- [ ] Configurar Firebase Genkit con API key
- [ ] Cargar base de conocimiento inicial
- [ ] Entrenar con conversaciones de ejemplo
- [ ] Configurar webhooks para actualizaciones
- [ ] Implementar cache para respuestas frecuentes
- [ ] Setup monitoring y alertas
- [ ] A/B testing de diferentes prompts
- [ ] Backup plan para fallback humano
- [ ] Compliance y privacidad de datos
- [ ] Load testing (>1000 conversaciones simultáneas)

---

## 📊 RESULTADOS ESPERADOS

| Métrica | Mes 1 | Mes 3 | Mes 6 |
|---------|-------|-------|-------|
| Consultas resueltas por IA | 40% | 60% | 75% |
| Reducción llamadas | -20% | -35% | -50% |
| Satisfacción cliente | 3.8/5 | 4.2/5 | 4.5/5 |
| Tiempo respuesta promedio | 3s | 2s | 1.5s |
| Costo por interacción | -30% | -45% | -60% |

---

*Documento creado: 2025-01-14*
*Versión: 1.0*
*Próxima revisión: Post-implementación fase 1*