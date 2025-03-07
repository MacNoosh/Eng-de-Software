
public class Pessoa {
    private String nome;
    private double altura;
    private int idade;
    private String profissao;
    private double salario;

    // Construtor
    public Pessoa(String nome, double altura, int idade, String profissao, double salario) {
        this.nome = nome;
        this.altura = altura;
        this.idade = idade;
        this.profissao = profissao;
        this.salario = salario;
    }

    // Método para mostrar o salário
    public double mostrarSalario() {
        return this.salario;
    }

    // Método para exibir informações
    public void exibirInformacoes() {
        System.out.println("A pessoa cadastrada é " + this.nome);
        System.out.println("Altura: " + this.altura);
        System.out.println("Idade: " + this.idade);
        System.out.println("Profissão: " + this.profissao);
        System.out.println("Salário: R$ " + this.salario);
    }

    public static void main(String[] args) {
        // Criando um objeto Pessoa
        Pessoa pessoa1 = new Pessoa("Zé", 1.80, 29, "Desenvolvedor", 9000.00);
        
        // Exibindo informações
        pessoa1.exibirInformacoes();
    }
}
