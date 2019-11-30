import random

from project.nqueen.functions import generate_empty_board


def init_genes(n, population_size):
    return [[random.randint(0, n-1) for _ in range(n)] for _ in range(population_size)]


def set_queens_for_gene(board, gene):
    for col_idx, chromosome in enumerate(gene):
        board[chromosome][col_idx] = 1
    return board


def reset_queens_for_gene(board, gene):
    for col_idx, chromosome in enumerate(gene):
        board[chromosome][col_idx] = 0
    return board


def calculate_fitness(board, n, max_fitness, gene):
    hits = 0
    for col_idx, chromosome in enumerate(gene):
        i, j = chromosome, col_idx
        while i > 0 and j < n-1:
            if board[i-1][j+1] == 1:
                hits += 1
            i -= 1
            j += 1
        i, j = chromosome, col_idx

        while i < n-1 and j < n-1:
            if board[i+1][j+1] == 1:
                hits += 1
            i += 1
            j += 1
        j = col_idx

        while j < n-1:
            if board[chromosome][j+1] == 1:
                hits += 1
            j += 1

    return max_fitness-hits


def mutate_gen(genes, n):
    for gene in genes:
        is_mutate = random.randint(0, 1)
        if is_mutate:
            mutate_idx = random.randint(0, n-1)
            gene[mutate_idx] = random.randint(0, n-1)


def swap_of_genes(genes, n):
    for i in range(1, n-2):
        genes[i+1] = genes[i]

    tmp = genes[0]
    genes[0] = genes[1]
    genes[1] = tmp


def selection_of_genes(genes, n):
    if n % 2 != 0:
        genes[-1] = genes[0]

    for i in range(0, n-1, 2):
        selection = random.randint(1, n-1)
        tmp = genes[i]
        genes[i] = genes[i][0:selection] + genes[i+1][selection:]
        genes[i+1] = genes[i+1][0:selection] + tmp[selection:]


def evaluate_genes(board, n, max_fitness, genes):
    evaluation = []
    for gene in genes:
        set_queens_for_gene(board, gene)
        fitness = calculate_fitness(board, n, max_fitness, gene)
        evaluation.append(fitness)
        reset_queens_for_gene(board, gene)

    evaluation, genes = (list(t) for t in zip(*sorted(zip(evaluation, genes), reverse=True)))
    return evaluation


def solve_genetic(board, genes, n):
    max_fitness = sum(range(n))
    population = 0
    solution_found = False

    while not solution_found:
        evaluation = evaluate_genes(board, n, max_fitness, genes)
        swap_of_genes(genes, n)
        selection_of_genes(genes, n)
        mutate_gen(genes, n)

        print(f'Population {str(population)}')
        for idx, gene in enumerate(genes):
            print(f'Gene: {str(gene)} | Fitness: {evaluation[idx]}')
        population += 1

        if max_fitness in evaluation:
            solution_found = True
            print(genes[0])


dimension = 17
popu_size = 20
brd = generate_empty_board(dimension)
gns = init_genes(dimension, popu_size)
solve_genetic(brd, gns, dimension)
