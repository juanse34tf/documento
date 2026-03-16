// Archivo: Paquete.java
package pk01;

import java.time.LocalDate;

class Paquete {
    private int codigoSeguimiento;
    private double peso;
    private String destino;
    private String estado;
    private LocalDate fechaEnvio;

    public Paquete() {
        this.codigoSeguimiento = 0;
        this.destino = "";
        this.estado = "Registrado";
        this.fechaEnvio = LocalDate.now();
    }

    public int getCodigo() {
        return codigoSeguimiento;
    }

    public void setCodigo(int codigoSeguimiento) {
        this.codigoSeguimiento = codigoSeguimiento;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public String getDestino() {
        return destino;
    }

    public void setDestino(String destino) {
        this.destino = destino;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    public LocalDate getFechaEnvio() {
        return fechaEnvio;
    }
}

// Archivo: Principal.java
package pk01;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Principal {
    public static void main(String[] args) {
        int tam = Integer.parseInt(JOptionPane.showInputDialog("CUÁNTOS PAQUETES VA A INGRESAR?"));
        Paquete paquetito[] = new Paquete[tam];
        
        for (int k = 0; k < tam; k++) {
            paquetito[k] = new Paquete();
            paquetito[k].setCodigo(Integer.parseInt(JOptionPane.showInputDialog("DIGITE CÓDIGO")));
            paquetito[k].setPeso(Double.parseDouble(JOptionPane.showInputDialog("DIGITE PESO (kg)")));
            paquetito[k].setDestino(JOptionPane.showInputDialog("DIGITE DESTINO"));
            paquetito[k].setEstado(JOptionPane.showInputDialog("DIGITE ESTADO INICIAL"));
        }
        
        Scanner scanner = new Scanner(System.in);
        int opcion = 0;
        
        while (opcion != 5) {
            System.out.println("\n--- MENÚ DE OPCIONES ---");
            System.out.println("1. Mostrar todos los paquetes");
            System.out.println("2. Actualizar estado de un paquete");
            System.out.println("3. Mostrar paquete más pesado");
            System.out.println("4. Listar paquetes con destino a Cali");
            System.out.println("5. Salir");
            System.out.print("Ingrese una opción: ");
            
            opcion = scanner.nextInt();
            
            switch (opcion) {
                case 1:
                    MostrarPaquetes.mostrar(paquetito);
                    break;
                case 2:
                    ActualizarEstado.actualizar(paquetito, scanner);
                    break;
                case 3:
                    MostrarMasPesado.mostrar(paquetito);
                    break;
                case 4:
                    MostrarDestino.mostrarCali(paquetito);
                    break;
                case 5:
                    System.out.println("Programa finalizado.");
                    break;
                default:
                    System.out.println("Opción inválida, intente nuevamente.");
            }
        }
        
        scanner.close();
    }
}

// Archivo: MostrarPaquetes.java
package pk01;

class MostrarPaquetes {
    public static void mostrar(Paquete[] paquetes) {
        System.out.println("\n--- LISTA DE TODOS LOS PAQUETES ---");
        for (int i = 0; i < paquetes.length; i++) {
            System.out.println("Paquete #" + (i+1));
            System.out.println("Código: " + paquetes[i].getCodigo());
            System.out.println("Peso: " + paquetes[i].getPeso() + " kg");
            System.out.println("Destino: " + paquetes[i].getDestino());
            System.out.println("Estado: " + paquetes[i].getEstado());
            System.out.println("Fecha de envío: " + paquetes[i].getFechaEnvio());
            System.out.println("-----------------------");
        }
    }
}

// Archivo: ActualizarEstado.java
package pk01;

import java.util.Scanner;

class ActualizarEstado {
    public static void actualizar(Paquete[] paquetes, Scanner scanner) {
        System.out.print("\nIngrese el código del paquete a actualizar: ");
        int codigo = scanner.nextInt();
        scanner.nextLine();
        
        boolean encontrado = false;
        for (Paquete paquete : paquetes) {
            if (paquete.getCodigo() == codigo) {
                System.out.print("Ingrese el nuevo estado del paquete: ");
                String nuevoEstado = scanner.nextLine();
                paquete.setEstado(nuevoEstado);
                System.out.println("Estado actualizado correctamente.");
                encontrado = true;
                break;
            }
        }
        
        if (!encontrado) {
            System.out.println("No se encontró ningún paquete con ese código.");
        }
    }
}

// Archivo: MostrarMasPesado.java
package pk01;

class MostrarMasPesado {
    public static void mostrar(Paquete[] paquetes) {
        if (paquetes.length == 0) {
            System.out.println("\nNo hay paquetes registrados.");
            return;
        }
        
        Paquete masPesado = paquetes[0];
        for (int i = 1; i < paquetes.length; i++) {
            if (paquetes[i].getPeso() > masPesado.getPeso()) {
                masPesado = paquetes[i];
            }
        }
        
        System.out.println("\n--- PAQUETE MÁS PESADO ---");
        System.out.println("Código: " + masPesado.getCodigo() + " | Peso: " + masPesado.getPeso() + " kg");
    }
}

// Archivo: MostrarDestino.java
package pk01;

class MostrarDestino {
    public static void mostrarCali(Paquete[] paquetes) {
        System.out.println("\n--- PAQUETES CON DESTINO A CALI ---");
        boolean hayPaquetes = false;
        
        for (Paquete paquete : paquetes) {
            if (paquete.getDestino().equalsIgnoreCase("Cali")) {
                System.out.println("Código: " + paquete.getCodigo());
                System.out.println("Peso: " + paquete.getPeso() + " kg");
                System.out.println("Estado: " + paquete.getEstado());
                System.out.println("Fecha de envío: " + paquete.getFechaEnvio());
                System.out.println("-----------------------");
                hayPaquetes = true;
            }
        }
        
        if (!hayPaquetes) {
            System.out.println("No hay paquetes con destino a Cali.");
        }
    }
}