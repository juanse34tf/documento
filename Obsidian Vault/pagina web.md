¡Listo! Vi tu captura: ya tienes varios archivos pero con nombres “VersionX”. Te dejo un plan claro para que GitHub Copilot (en VS Code) y tú lo dejen prolijo, profesional y listo para correr local, subir a GitHub y desplegar en Heroku.

Resumen de lo que haremos:
- Normalizar nombres de archivos (quitar “_VersionX”).
- Crear carpetas y archivos faltantes con contenido profesional.
- Instalar dependencias y correr local (dev y prod).
- Subir a GitHub.
- Desplegar a Heroku.

PARTE 1) Renombrar archivos que ya tienes
Usa PowerShell integrado de VS Code (Terminal > New Terminal) y ejecuta esto para renombrar si existen. No falla si algún archivo no existe.

```powershell
# Ejecuta desde la carpeta raíz del proyecto (donde está package.json)
# Renombrar archivos versión -> nombre final
$ErrorActionPreference="SilentlyContinue"

Rename-Item "editorconfig_Version2.txt" ".editorconfig"
Rename-Item "eslintrc_Version2.json" ".eslintrc.json"
Rename-Item "gitignore_Version4.txt" ".gitignore"
Rename-Item "prettierrc_Version2.txt" ".prettierrc"
Rename-Item "Procfile_Version4.txt" "Procfile"
Rename-Item "server_Version4.js" "server.js"
Rename-Item "tailwind.config_Version4.js" "tailwind.config.js"
Rename-Item "tsconfig_Version3.json" "tsconfig.json"
Rename-Item "vite.config_Version2.ts" "vite.config.ts"
Rename-Item "postcss.config_Version3.js" "postcss.config.js"
Rename-Item "index_Version4.html" "index.html"
```

Opcional: borra duplicados viejos que ya no se usan (los con “_VersionX” que queden).

PARTE 2) Dile a GitHub Copilot qué debe hacer
Abre la pestaña “Copilot Chat” en VS Code y pega este prompt. Copilot generará/ajustará archivos. Si algo no lo crea, crea el archivo y pega el contenido que te dejo abajo.

Prompt para Copilot (pégalo tal cual):
Crea/actualiza un proyecto React + Vite + TypeScript con Tailwind, Framer Motion y React Icons, listo para Heroku con Express. 
1) Asegúrate de estos archivos con exactamente este contenido (si existen, sobrescríbelos): package.json, tsconfig.json, vite.config.ts, postcss.config.js, tailwind.config.js, .gitignore, .editorconfig, .eslintrc.json, .prettierrc, Procfile, server.js, index.html. 
2) Crea carpetas: src/components, src/utils, public. 
3) Crea estos archivos con el contenido que te voy a dar (o usa el que ya pusimos si coincide): src/index.css, src/main.tsx, src/App.tsx, src/components/Header.tsx, src/components/Hero.tsx, src/components/Services.tsx, src/components/Cases.tsx, src/components/Footer.tsx, src/components/Loading.tsx, src/components/ScrollToTopButton.tsx, src/utils/animations.ts, public/robots.txt, public/sitemap.xml, public/manifest.webmanifest, public/sw.js, README.md, LICENSE, .env.example. 
4) Instala dependencias con npm install. 
5) Ejecuta npm run dev y verifica http://localhost:5173. Luego build y prod local con npm run build && npm start en http://localhost:3000.

PARTE 3) Contenidos canónicos de todos los archivos
Copia/pega exactamente estos archivos si Copilot no los crea bien. Están listos para producción y Heroku.

```json name=package.json
{
  "name": "juanse-tech-web",
  "version": "1.1.0",
  "private": true,
  "description": "juanse.tech - Automatización IA Enterprise: Bots WhatsApp, Integración APIs, Analytics",
  "engines": { "node": "20.x" },
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "start": "node server.js",
    "heroku-postbuild": "npm run build",
    "lint": "eslint . --ext .ts,.tsx --max-warnings=0",
    "format": "prettier . --write"
  },
  "dependencies": {
    "compression": "^1.7.4",
    "express": "^4.19.2",
    "framer-motion": "^11.0.0",
    "helmet": "^7.1.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-icons": "^4.12.0"
  },
  "devDependencies": {
    "@types/compression": "^1.7.5",
    "@types/express": "^4.17.21",
    "@types/node": "^20.11.30",
    "@types/react": "^18.2.25",
    "@types/react-dom": "^18.2.11",
    "@typescript-eslint/eslint-plugin": "^7.0.0",
    "@typescript-eslint/parser": "^7.0.0",
    "autoprefixer": "^10.4.15",
    "eslint": "^8.57.0",
    "eslint-config-prettier": "^9.1.0",
    "eslint-plugin-react": "^7.34.1",
    "postcss": "^8.4.31",
    "prettier": "^3.2.5",
    "tailwindcss": "^3.4.3",
    "typescript": "^5.4.5",
    "vite": "^5.2.0"
  }
}
```

```json name=tsconfig.json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["DOM", "DOM.Iterable", "ES2022"],
    "allowJs": false,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "module": "ESNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "types": ["node", "react", "react-dom"]
  },
  "include": ["src", "vite-env.d.ts"]
}
```

```typescript name=vite.config.ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  build: {
    target: "es2019",
    sourcemap: false,
    chunkSizeWarningLimit: 800,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ["react", "react-dom", "framer-motion"]
        }
      }
    }
  }
});
```

```javascript name=postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {}
  }
};
```

```javascript name=tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: { inter: ["Inter", "sans-serif"] },
      colors: {
        primary: "#1e3a8a",
        brand: { DEFAULT: "#2563eb", light: "#60a5fa", dark: "#1e3a8a" }
      },
      backgroundImage: {
        "hero-gradient": "linear-gradient(135deg,#2563eb 0%,#60a5fa 100%)"
      },
      boxShadow: { glass: "0 8px 32px 0 rgba(31,38,135,0.37)" }
    }
  },
  plugins: []
};
```

```gitignore name=.gitignore
node_modules
dist
dist-ssr
*.log
npm-debug.log*
yarn-error.log
.pnpm-debug.log
.env
.env.local
.DS_Store
.idea
.vscode
*.swp
coverage
```

```editorconfig name=.editorconfig
root = true
[*]
charset = utf-8
end_of_line = lf
indent_style = space
indent_size = 2
insert_final_newline = true
trim_trailing_whitespace = true
[*.md]
max_line_length = off
```

```json name=.eslintrc.json
{
  "root": true,
  "env": { "browser": true, "es2022": true, "node": true },
  "parser": "@typescript-eslint/parser",
  "parserOptions": { "ecmaVersion": "latest", "sourceType": "module" },
  "settings": { "react": { "version": "detect" } },
  "plugins": ["react", "@typescript-eslint"],
  "extends": [
    "eslint:recommended",
    "plugin:react/recommended",
    "plugin:@typescript-eslint/recommended",
    "eslint-config-prettier"
  ],
  "rules": {
    "react/react-in-jsx-scope": "off",
    "@typescript-eslint/no-unused-vars": ["warn", { "argsIgnorePattern": "^_", "varsIgnorePattern": "^_" }],
    "react/prop-types": "off"
  }
}
```

```json name=.prettierrc
{
  "printWidth": 90,
  "singleQuote": false,
  "semi": true,
  "trailingComma": "none"
}
```

```bash name=Procfile
web: npm start
```

```javascript name=server.js
import express from "express";
import path from "path";
import compression from "compression";
import helmet from "helmet";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const app = express();

app.use(helmet({ contentSecurityPolicy: false }));
app.disable("x-powered-by");
app.use(compression());

const distPath = path.join(__dirname, "dist");
app.use(
  express.static(distPath, {
    setHeaders: (res, filePath) => {
      if (filePath.endsWith(".html")) res.setHeader("Cache-Control", "no-cache");
      else res.setHeader("Cache-Control", "public, max-age=31536000, immutable");
    }
  })
);

app.get("/health", (_req, res) => res.json({ status: "ok", uptime: process.uptime() }));

app.get("*", (_req, res) => res.sendFile(path.join(distPath, "index.html")));

const port = process.env.PORT || 3000;
app.listen(port, () => console.log("juanse.tech app corriendo en puerto " + port));
```

```html name=index.html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <link rel="icon" href="/favicon.ico" />
  <link rel="manifest" href="/manifest.webmanifest" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>juanse.tech | Automatización IA Enterprise</title>
  <meta name="description" content="Automatización IA Enterprise: Bots WhatsApp, Integración APIs y Analytics avanzados para empresas." />
  <meta name="keywords" content="automatización, IA, enterprise, bots WhatsApp, APIs, analytics, integración, inteligencia artificial, juanse.tech" />
  <meta name="theme-color" content="#2563eb" />
  <link rel="canonical" href="https://juanse.tech/" />
  <meta property="og:title" content="juanse.tech - Automatización IA Enterprise" />
  <meta property="og:description" content="Bots WhatsApp, Integración APIs y Analytics impulsados por IA." />
  <meta property="og:image" content="/og-image.png" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://juanse.tech/" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="juanse.tech - Automatización IA Enterprise" />
  <meta name="twitter:description" content="Soluciones IA escalables para tu organización." />
  <meta name="twitter:image" content="/og-image.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <script type="application/ld+json">
  {
    "@context":"https://schema.org",
    "@type":"Organization",
    "name":"juanse.tech",
    "url":"https://juanse.tech",
    "email":"contacto@juanse.tech",
    "description":"Automatización IA Enterprise: Bots WhatsApp, Integración APIs y Analytics.",
    "logo":"https://juanse.tech/og-image.png",
    "sameAs":[
      "https://www.linkedin.com/in/tu-linkedin",
      "https://github.com/tu-github"
    ]
  }
  </script>
</head>
<body class="bg-gradient-to-br from-primary to-brand.dark text-white font-inter antialiased selection:bg-brand.light/70 selection:text-primary relative">
  <a href="#main" class="absolute left-2 top-2 -translate-y-20 focus:translate-y-0 bg-brand.light text-primary font-semibold px-4 py-2 rounded transition">Saltar al contenido</a>
  <div id="root"></div>
  <script type="module" src="/src/main.tsx"></script>
</body>
</html>
```

```css name=src/index.css
@tailwind base;
@tailwind components;
@tailwind utilities;

body { font-family: 'Inter', system-ui, sans-serif; }

.glassmorphism {
  background: rgba(37, 99, 235, 0.15);
  box-shadow: 0 8px 32px 0 rgba(31,38,135,0.37);
  backdrop-filter: blur(14px);
  border-radius: 1.4rem;
  border: 1px solid rgba(255,255,255,0.18);
}

::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: #1e3a8a40; }
::-webkit-scrollbar-thumb { background: linear-gradient(#2563eb,#60a5fa); border-radius: 8px; }
```

```typescript name=src/main.tsx
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

```typescript name=src/App.tsx
import React, { Suspense, lazy } from "react";
import { AnimatePresence } from "framer-motion";
import Header from "./components/Header";
import Hero from "./components/Hero";
import Footer from "./components/Footer";
import Loading from "./components/Loading";
import ScrollToTopButton from "./components/ScrollToTopButton";

const Services = lazy(() => import("./components/Services"));
const Cases = lazy(() => import("./components/Cases"));

function App() {
  return (
    <div className="flex flex-col min-h-screen">
      <AnimatePresence mode="wait">
        <Header />
        <Hero />
        <main id="main" className="flex-1 flex flex-col gap-28 pt-4 md:pt-16">
          <Suspense fallback={<Loading />}>
            <Services />
            <Cases />
          </Suspense>
        </main>
        <Footer />
        <ScrollToTopButton />
      </AnimatePresence>
    </div>
  );
}

export default App;
```

```typescript name=src/components/Header.tsx
import React from "react";
import { motion } from "framer-motion";
import { FaRobot, FaEnvelope } from "react-icons/fa";
import { fadeDown } from "../utils/animations";

const navLinks = [
  { label: "Servicios", href: "#servicios" },
  { label: "Casos de Éxito", href: "#casos" },
  { label: "Contacto", href: "mailto:contacto@juanse.tech" }
];

function Header() {
  return (
    <motion.header
      variants={fadeDown}
      initial="initial"
      animate="animate"
      className="fixed top-0 left-0 right-0 z-50 glassmorphism px-5 md:px-16 py-3 flex items-center justify-between backdrop-saturate-150"
      role="banner"
    >
      <a
        href="/"
        aria-label="Inicio juanse.tech"
        className="flex items-center gap-2 font-extrabold text-lg md:text-xl tracking-tight hover:text-brand.light transition-colors"
      >
        <FaRobot className="text-brand.light text-2xl drop-shadow" />
        juanse.<span className="text-brand.light">tech</span>
      </a>
      <nav className="hidden md:flex gap-10" aria-label="Navegación principal">
        {navLinks.map((l) => (
          <a
            key={l.label}
            href={l.href}
            className="relative group font-semibold hover:text-brand.light transition-colors"
          >
            {l.label}
            <span className="absolute left-0 -bottom-1 h-0.5 w-0 bg-brand.light transition-all group-hover:w-full"></span>
          </a>
        ))}
      </nav>
      <a
        href="mailto:contacto@juanse.tech"
        aria-label="Enviar correo"
        className="md:hidden rounded-full p-2 hover:bg-brand.light/20 transition"
      >
        <FaEnvelope className="text-xl text-brand.light" />
      </a>
    </motion.header>
  );
}

export default Header;
```

```typescript name=src/components/Hero.tsx
import React from "react";
import { motion } from "framer-motion";
import { FaWhatsapp, FaCode, FaChartLine } from "react-icons/fa";
import { staggerContainer, fadeUp } from "../utils/animations";

const headline = "Automatización IA Enterprise";
const subheadline =
  "Soluciones integrales de automatización y analítica potenciadas por IA para empresas líderes.";
const cta = "Solicitar Demo Gratis";

function Hero() {
  return (
    <section
      className="relative min-h-[85vh] flex items-center justify-center pt-28 md:pt-36"
      aria-labelledby="hero-heading"
    >
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 0.9 }}
        transition={{ duration: 1.2 }}
        className="absolute inset-0 -z-10"
      >
        <motion.div
          initial={{ scale: 1.05 }}
          animate={{
            scale: [1.05, 1.15, 1.08],
            rotate: [0, 2, -2, 0],
            filter: ["blur(70px)", "blur(110px)", "blur(70px)"]
          }}
          transition={{ duration: 14, repeat: Infinity, ease: "easeInOut" }}
          className="absolute left-1/2 top-1/3 w-[78vw] h-[62vh] -translate-x-1/2 rounded-3xl bg-hero-gradient opacity-70"
        />
      </motion.div>
      <motion.div
        variants={staggerContainer}
        initial="initial"
        animate="animate"
        className="relative z-10 flex flex-col items-center text-center max-w-2xl mx-auto px-5"
      >
        <motion.h1
          id="hero-heading"
          variants={fadeUp}
          className="text-3xl md:text-5xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-brand.light to-white drop-shadow-sm leading-tight"
        >
          {headline}
        </motion.h1>
        <motion.p variants={fadeUp} className="mt-6 text-lg md:text-xl font-medium text-white/90">
          {subheadline}
        </motion.p>
        <motion.div variants={fadeUp} className="mt-10 flex flex-col items-center gap-5 w-full">
          <motion.a
            whileHover={{ scale: 1.07 }}
            whileTap={{ scale: 0.96 }}
            href="mailto:contacto@juanse.tech?subject=Solicitar%20Demo"
            className="inline-block px-8 py-3 rounded-2xl font-semibold text-lg bg-brand.light text-primary shadow-lg glassmorphism hover:shadow-xl transition-all focus:outline-none focus-visible:ring-4 focus-visible:ring-brand.light/50"
          >
            {cta}
          </motion.a>
          <div className="flex flex-wrap gap-4 justify-center">
            <div className="flex items-center gap-2 text-sm bg-white/10 px-4 py-2 rounded-xl glassmorphism hover:scale-105 transition">
              <FaWhatsapp className="text-brand.light" /> Bots WhatsApp
            </div>
            <div className="flex items-center gap-2 text-sm bg-white/10 px-4 py-2 rounded-xl glassmorphism hover:scale-105 transition">
              <FaCode className="text-brand.light" /> Integración APIs
            </div>
            <div className="flex items-center gap-2 text-sm bg-white/10 px-4 py-2 rounded-xl glassmorphism hover:scale-105 transition">
              <FaChartLine className="text-brand.light" /> Analytics IA
            </div>
          </div>
        </motion.div>
      </motion.div>
    </section>
  );
}

export default Hero;
```

```typescript name=src/components/Services.tsx
import React from "react";
import { motion } from "framer-motion";
import { FaWhatsapp, FaCode, FaChartBar } from "react-icons/fa";
import { fadeInOnScroll } from "../utils/animations";

const services = [
  { icon: <FaWhatsapp className="text-3xl text-brand.light" />, title: "Bots WhatsApp", desc: "Automatiza la atención y gestión de pedidos en WhatsApp con IA avanzada." },
  { icon: <FaCode className="text-3xl text-brand.light" />, title: "Integración APIs", desc: "Conecta sistemas empresariales y plataformas externas de forma segura y escalable." },
  { icon: <FaChartBar className="text-3xl text-brand.light" />, title: "Analytics IA", desc: "Dashboards y reportes inteligentes para decisiones basadas en datos." }
];

function Services() {
  return (
    <section id="servicios" aria-labelledby="servicios-title" className="w-full px-5 md:px-0 max-w-6xl mx-auto">
      <motion.div initial="initial" whileInView="animate" viewport={{ once: true, amount: 0.3 }} className="flex flex-col items-center">
        <motion.h2 variants={fadeInOnScroll} id="servicios-title" className="text-2xl md:text-3xl font-bold mb-10 text-center bg-gradient-to-r from-brand.light to-white text-transparent bg-clip-text">
          Servicios IA que impulsan tu empresa
        </motion.h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-10 w-full">
          {services.map((srv, idx) => (
            <motion.div
              key={srv.title}
              variants={fadeInOnScroll}
              custom={idx}
              className="glassmorphism p-8 flex flex-col items-center text-center shadow-lg hover:shadow-2xl hover:scale-105 transition-all cursor-pointer group focus-within:ring-2 focus-within:ring-brand.light/60"
              whileHover={{ scale: 1.06, boxShadow: "0 12px 40px 0 rgba(31,38,135,0.35)" }}
              tabIndex={0}
            >
              <div className="mb-4">{srv.icon}</div>
              <h3 className="text-lg font-semibold mb-2">{srv.title}</h3>
              <p className="text-white/80 leading-relaxed">{srv.desc}</p>
            </motion.div>
          ))}
        </div>
      </motion.div>
    </section>
  );
}

export default Services;
```

```typescript name=src/components/Cases.tsx
import React from "react";
import { motion } from "framer-motion";
import { FaUtensils, FaBuilding } from "react-icons/fa";
import { fadeInOnScroll } from "../utils/animations";

const cases = [
  { icon: <FaUtensils className="text-2xl text-brand.light" />, title: "Cadena de restaurantes", result: "+40% pedidos automatizados", desc: "Bots WhatsApp optimizaron pedidos y reservas mejorando tiempos de respuesta.", bg: "from-primary/80 to-brand.light/60" },
  { icon: <FaBuilding className="text-2xl text-brand.light" />, title: "Inmobiliaria", result: "+60% leads generados", desc: "Integración de APIs y analytics IA calificó leads automáticamente.", bg: "from-brand.dark/80 to-primary/60" }
];

function Cases() {
  return (
    <section id="casos" aria-labelledby="casos-title" className="w-full px-5 md:px-0 max-w-6xl mx-auto">
      <motion.div initial="initial" whileInView="animate" viewport={{ once: true, amount: 0.25 }} className="flex flex-col items-center">
        <motion.h2 variants={fadeInOnScroll} id="casos-title" className="text-2xl md:text-3xl font-bold mb-10 text-center bg-gradient-to-r from-brand.light to-white text-transparent bg-clip-text">
          Casos de Éxito
        </motion.h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-10 w-full">
          {cases.map((caso, idx) => (
            <motion.div
              key={caso.title}
              variants={fadeInOnScroll}
              custom={idx}
              whileHover={{ scale: 1.05, boxShadow: "0 8px 28px 0 rgba(31,38,135,0.30)" }}
              className={`relative glassmorphism p-8 flex flex-col gap-4 shadow-lg transition-all group overflow-hidden bg-gradient-to-br ${caso.bg}`}
            >
              <motion.div className="absolute -top-6 -right-6 opacity-10 blur-xl" animate={{ y: [0, 12, -12, 0] }} transition={{ duration: 7, repeat: Infinity, ease: "easeInOut" }}>
                {caso.icon}
              </motion.div>
              <div className="flex items-center gap-3 z-10">{caso.icon}<span className="font-semibold text-lg">{caso.title}</span></div>
              <div className="z-10 text-brand.light font-bold text-xl">{caso.result}</div>
              <p className="z-10 text-white/90 leading-relaxed">{caso.desc}</p>
            </motion.div>
          ))}
        </div>
      </motion.div>
    </section>
  );
}

export default Cases;
```

```typescript name=src/components/Footer.tsx
import React from "react";
import { FaLinkedin, FaEnvelope, FaGithub } from "react-icons/fa";

const links = [
  { icon: <FaLinkedin />, href: "https://www.linkedin.com/in/tu-linkedin", label: "LinkedIn" },
  { icon: <FaGithub />, href: "https://github.com/tu-github", label: "GitHub" },
  { icon: <FaEnvelope />, href: "mailto:contacto@juanse.tech", label: "Email" }
];

function Footer() {
  return (
    <footer className="mt-24 py-10 px-6 md:px-16 glassmorphism flex flex-col md:flex-row items-center justify-between gap-6 text-white/90 relative z-20" role="contentinfo">
      <div className="text-base md:text-lg font-bold flex items-center gap-2">
        juanse.<span className="text-brand.light">tech</span>
        <span className="text-xs font-normal ml-2">© {new Date().getFullYear()} - Automatización IA Enterprise</span>
      </div>
      <nav className="flex gap-8" aria-label="Redes">
        {links.map((link) => (
          <a key={link.label} href={link.href} target="_blank" rel="noopener noreferrer" className="text-brand.light text-2xl hover:scale-125 transition-all focus-visible:ring-4 focus-visible:ring-brand.light/40 rounded" aria-label={link.label}>
            {link.icon}
          </a>
        ))}
      </nav>
    </footer>
  );
}

export default Footer;
```

```typescript name=src/components/Loading.tsx
import React from "react";
import { motion } from "framer-motion";

function Loading() {
  return (
    <div className="flex justify-center items-center min-h-[30vh]" role="status" aria-label="Cargando">
      <motion.div className="w-16 h-16 rounded-full bg-brand.light/30 flex items-center justify-center shadow-inner" animate={{ rotate: 360 }} transition={{ repeat: Infinity, duration: 1.4, ease: "linear" }}>
        <motion.div className="w-8 h-8 rounded-full border-4 border-brand.light border-t-transparent" animate={{ rotate: 360 }} transition={{ repeat: Infinity, duration: 0.8, ease: "linear" }} />
      </motion.div>
    </div>
  );
}

export default Loading;
```

```typescript name=src/components/ScrollToTopButton.tsx
import React, { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { FaArrowUp } from "react-icons/fa";

function ScrollToTopButton() {
  const [visible, setVisible] = useState(false);
  useEffect(() => {
    const onScroll = () => setVisible(window.scrollY > 450);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <AnimatePresence>
      {visible && (
        <motion.button
          initial={{ opacity: 0, y: 80 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: 80 }}
          whileHover={{ scale: 1.12 }}
          whileTap={{ scale: 0.9 }}
          onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
          aria-label="Volver arriba"
          className="fixed bottom-6 right-6 p-4 rounded-full bg-brand.light text-primary shadow-lg hover:shadow-2xl focus-visible:ring-4 focus-visible:ring-brand.light/50 transition"
        >
          <FaArrowUp />
        </motion.button>
      )}
    </AnimatePresence>
  );
}

export default ScrollToTopButton;
```

```typescript name=src/utils/animations.ts
import { Variants } from "framer-motion";

export const staggerContainer: Variants = {
  initial: {},
  animate: { transition: { staggerChildren: 0.2 } }
};

export const fadeUp: Variants = {
  initial: { opacity: 0, y: 40 },
  animate: { opacity: 1, y: 0, transition: { duration: 1, ease: "easeOut" } }
};

export const fadeDown: Variants = {
  initial: { opacity: 0, y: -40 },
  animate: { opacity: 1, y: 0, transition: { duration: 0.8, ease: "easeOut" } }
};

export const fadeInOnScroll: Variants = {
  initial: { opacity: 0, y: 60 },
  animate: (i = 0) => ({ opacity: 1, y: 0, transition: { duration: 0.9, ease: "easeOut", delay: 0.1 * i } })
};
```

```text name=public/robots.txt
User-agent: *
Allow: /
Sitemap: https://juanse.tech/sitemap.xml
```

```xml name=public/sitemap.xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://juanse.tech/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>
  <url><loc>https://juanse.tech/#servicios</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>
  <url><loc>https://juanse.tech/#casos</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>
</urlset>
```

```json name=public/manifest.webmanifest
{
  "name": "juanse.tech - Automatización IA Enterprise",
  "short_name": "juanse.tech",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#1e3a8a",
  "theme_color": "#2563eb",
  "description": "Bots WhatsApp, Integración APIs y Analytics impulsados por IA.",
  "icons": [
    { "src": "/icon-192.png", "type": "image/png", "sizes": "192x192" },
    { "src": "/icon-512.png", "type": "image/png", "sizes": "512x512" }
  ]
}
```

```javascript name=public/sw.js
self.addEventListener("install", (e) => { e.waitUntil(caches.open("static-v1").then((cache) => cache.addAll(["/", "/index.html"]))); });
self.addEventListener("fetch", (e) => { e.respondWith(caches.match(e.request).then((res) => res || fetch(e.request))); });
```

````markdown name=README.md
# juanse.tech - Automatización IA Enterprise

Bots WhatsApp · Integración APIs · Analytics IA.

## Comandos
| Script | Acción |
|--------|--------|
| `npm run dev` | Desarrollo (localhost:5173) |
| `npm run build` | Build producción en `dist/` |
| `npm start` | Servidor Express (producción local o Heroku) |
| `npm run lint` | Revisa código |
| `npm run format` | Formatea código |

## Pasos rápidos
```bash
npm install
npm run dev
npm run build
npm start
```

## Deploy Heroku
1. `heroku login`
2. `heroku create juanse-tech-web`
3. `git push heroku main`
4. `heroku open`
````

```text name=LICENSE
MIT License
(Cámbialo por tu nombre si quieres)
```

```env name=.env.example
VITE_ANALYTICS_KEY=tu_key
```

PARTE 4) Instalar y correr local en Windows
- Instala dependencias:
  - npm install
- Modo desarrollo:
  - npm run dev
  - Abre http://localhost:5173
- Producción local (simula Heroku):
  - npm run build
  - npm start
  - Abre http://localhost:3000

PARTE 5) Subir a GitHub
Reemplaza juanse34tf por tu usuario si cambia.

```powershell
git init
git add .
git commit -m "feat: sitio profesional juanse.tech listo para Heroku"
git branch -M main
git remote add origin https://github.com/juanse34tf/juanse-tech-web.git
# o SSH: git remote add origin git@github.com:juanse34tf/juanse-tech-web.git
git push -u origin main
```

PARTE 6) Desplegar en Heroku
```powershell
heroku login
heroku create juanse-tech-web
git push heroku main
heroku open
heroku logs --tail   # si necesitas ver logs
```

Notas finales importantes
- Asegúrate de poner tus enlaces reales en:
  - index.html (JSON-LD sameAs)
  - src/components/Footer.tsx (LinkedIn/GitHub)
- Coloca en public estos archivos gráficos:
  - favicon.ico, og-image.png (1200x630), icon-192.png, icon-512.png
- Si quieres PWA, registra el service worker en src/main.tsx (te digo cómo cuando lo quieras).

¿Quieres que ahora le pida a Copilot que agregue un Dark Mode o un formulario de contacto con envío a tu email? Dime cuál y lo automatizamos.