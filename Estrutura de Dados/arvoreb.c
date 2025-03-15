#include <stdio.h>
#include <stdlib.h>

#define T 3 // Grau mínimo da Arvore B (tamanho mínimo de chave por nó)

// Estrutura para representar um no da Árvore B
typedef struct NoB {
    int n; // Número de chaves atualmente no no
    int folha; // Indica se o no e uma folha (1) ou não (0)
    int chaves[2 * T - 1]; // Vetor de chaves
    struct NoB *filhos[2 * T]; // Vetor de ponteiros para os filhos
} NoB;

// Cria um novo no da Árvore B
NoB *criaNo(int folha) {
    NoB *no = (NoB *)malloc(sizeof(NoB));
    no->n = 0;
    no->folha = folha;
    for (int i = 0; i < 2 * T; i++) {
        no->filhos[i] = NULL;
    }
    return no;
}

// Percorre a Arvore B em ordem (similar ao in-order traversal)
void percorre(NoB *raiz) {
    if (raiz) {
        int i;
        for (i = 0; i < raiz->n; i++) {
            if (!raiz->folha) {
                percorre(raiz->filhos[i]);
            }
            printf("%d ", raiz->chaves[i]);
        }
        if (!raiz->folha) {
            percorre(raiz->filhos[i]);
        }
    }
}

// Função principal para inserir uma chave na Arvore B
void insereB(NoB **raiz, int chave);
void insereNaoCheio(NoB *no, int chave);
void divideFilho(NoB *pai, int i, NoB *filho);

void insereB(NoB **raiz, int chave) {
    NoB *r = *raiz;
    if (r->n == 2 * T - 1) { // Se a raiz estiver cheia, cria um novo nó
        NoB *s = criaNo(0);
        *raiz = s;
        s->filhos[0] = r;
        divideFilho(s, 0, r);
        insereNaoCheio(s, chave);
    } else {
        insereNaoCheio(r, chave);
    }
}

// Insere uma chave em um nó que não está cheio
void insereNaoCheio(NoB *no, int chave) {
    int i = no->n - 1;
    if (no->folha) {
        while (i >= 0 && chave < no->chaves[i]) {
            no->chaves[i + 1] = no->chaves[i];
            i--;
        }
        no->chaves[i + 1] = chave;
        no->n++;
    } else {
        while (i >= 0 && chave < no->chaves[i]) {
            i--;
        }
        i++;
        if (no->filhos[i]->n == 2 * T - 1) {
            divideFilho(no, i, no->filhos[i]);
            if (chave > no->chaves[i]) {
                i++;
            }
        }
        insereNaoCheio(no->filhos[i], chave);
    }
}

// Divide um nó filho cheio
void divideFilho(NoB *pai, int i, NoB *filho) {
    NoB *novo = criaNo(filho->folha);
    novo->n = T - 1;
    for (int j = 0; j < T - 1; j++) {
        novo->chaves[j] = filho->chaves[j + T];
    }
    if (!filho->folha) {
        for (int j = 0; j < T; j++) {
            novo->filhos[j] = filho->filhos[j + T];
        }
    }
    filho->n = T - 1;
    for (int j = pai->n; j >= i + 1; j--) {
        pai->filhos[j + 1] = pai->filhos[j];
    }
    pai->filhos[i + 1] = novo;
    for (int j = pai->n - 1; j >= i; j--) {
        pai->chaves[j + 1] = pai->chaves[j];
    }
    pai->chaves[i] = filho->chaves[T - 1];
    pai->n++;
}

// Programa principal
typedef struct ArvoreB {
    NoB *raiz;
} ArvoreB;

int main() {
    ArvoreB arvore;
    arvore.raiz = criaNo(1);
    
    int chaves[] = {9, 7, 12, 24, 3, 19, 15,17};
    for (int i = 0; i < 8; i++) {
        insereB(&arvore.raiz, chaves[i]);
    }
    
    printf("\nPercorrendo a Arvore B:\n");
    percorre(arvore.raiz);
    printf("\n");
    return 0;
}
