import java.util.Scanner;

public class Banco {
    // Atributos
    public String banco;
    public String agencia;
    public int conta;
    public String cliente;
    public String cpf;
    public double saldo;
    public double caixinha;
    public Integer tempo_investimento;
    public double taxajuros;
    public String senha;
    
    private static final Scanner scanner = new Scanner(System.in); // Scanner único

    // Método construtor
    public Banco(String banco, String agencia, int conta, String cliente, String cpf) {
        this.banco = banco;
        this.agencia = agencia;
        this.conta = conta;
        this.cliente = cliente;
        this.cpf = cpf;
        this.saldo = 0;
        this.caixinha = 0;
        this.tempo_investimento = null;
        this.taxajuros = 0.005;
        this.senha = null;
    }

    // Método para definir senha
    public void definirSenha(String novasenha) {
        if (this.senha == null) {
            this.senha = novasenha;
            System.out.println("Sua senha foi definida");
        } else {
            System.out.print("Você já possui uma senha definida, deseja alterar sua senha? (sim/não): ");
            String decisao = scanner.nextLine().toLowerCase();
            if (decisao.equals("sim")) {
                this.senha = novasenha;
                System.out.println("Senha alterada com sucesso");
            } else {
                System.out.println("Opção cancelada");
            }
        }
    }

    // Método de depósito
    public void deposito(double valor) {
        if (valor > 0) {
            this.saldo += valor;
            System.out.printf("Saldo atualizado com sucesso no valor R$%.2f.\n", valor);
        } else {
            System.out.println("Valor inválido para o depósito");
        }
    }

    // Método de saque
    public void saque(String senha, double valor) {
        if (this.senha.equals(senha) && this.saldo >= valor && valor > 0) {
            this.saldo -= valor;
            System.out.printf("Saque realizado no valor de: R$%.2f.\n", valor);
        } else {
            System.out.println("Valor ou senha incorretos, tente novamente");
        }
    }

    // Método PIX
    public void pix(Banco destinatario, double valor) {
        if (valor > 0 && this.saldo >= valor) {
            this.saldo -= valor;
            destinatario.saldo += valor;
            System.out.printf("PIX realizado no valor R$%.2f\nDE: %s\nPARA: %s\n", valor, this.cliente, destinatario.cliente);
        } else {
            System.out.println("Valor inválido ou saldo insuficiente para a transferência");
        }
    }

    // Método para investir na caixinha
    public void caixinhaInvest(double valor, int tempoMeses) {
        if (valor > 0 && this.saldo >= valor) {
            this.saldo -= valor;
            this.caixinha += valor;
            this.tempo_investimento = tempoMeses;
            System.out.printf("Valor de R$%.2f transferido para a caixinha por %d meses.\n", valor, tempoMeses);
        } else {
            System.out.println("Valor inválido ou saldo insuficiente para o investimento");
        }
    }

    // Método para calcular rendimento
    public void calcularRendimento() {
        if (this.tempo_investimento != null && this.caixinha > 0) {
            double montante = this.caixinha * Math.pow(1 + this.taxajuros, this.tempo_investimento);
            double rendimento = montante - this.caixinha;
            this.caixinha = montante;
            System.out.printf("Rendimento da caixinha após %d meses: R$%.2f\n", this.tempo_investimento, rendimento);
        } else {
            System.out.println("Não há investimento ou caixinha menor que zero");
        }
    }
    
    // Método extrato
    public void extrato() {
        System.out.println(
            "-----------------------------------------------------------------------\n" +
            "Conta: " + this.conta + "\n" +
            "Agência: " + this.agencia + "\n" +
            "Saldo: R$" + String.format("%.2f", this.saldo) + "\n" +
            "Cliente: " + this.cliente + "\n" +
            "-----------------------------------------------------------------------"
        );
    }

    public static void main(String[] args) throws InterruptedException {
        Banco cliente1 = new Banco("Moeda Saqua", "0001", 101049, "Raphael Oliveira", "14451043778");
        cliente1.definirSenha("admin");
        cliente1.deposito(5000);
        cliente1.caixinhaInvest(2500, 12);
        cliente1.extrato();
        
        // Simular 12 meses depois
        System.out.println("12 meses depois ......");
        Thread.sleep(2000);
        cliente1.calcularRendimento();
        cliente1.extrato();

        // Simulando outro cliente
        Banco cliente2 = new Banco("Banco Invest", "0005", 281090, "Thamiris Melo", "12724415233");
        cliente2.definirSenha("124");
        cliente2.deposito(6000);
        
        cliente1.pix(cliente2, 1500);
        
        cliente1.extrato();
        cliente2.extrato();
    }
}