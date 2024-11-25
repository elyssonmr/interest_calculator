from decimal import Decimal

from simulation.fixed_income import (
    FixedInterestSimulator,
    FixedInterestDataSimulator
)

EXIT_OPTION = 3

option = 0

while option != EXIT_OPTION:
    print('Opções:')
    print('1. Simulação de juros compostos')
    print('2. Gerar CSV da simulação de juros compostos')
    print('3. Sair')

    option = int(input('Escolha uma opção: '))
    print()

    match option:
        case 1:
            initial_amount = Decimal(
                input('Valor Inicial (use 0 caso não queira usar): ')
            )
            monthly_contribution = Decimal(
                input('Aportes Mensais (use 0 caso não queira usar): ')
            )
            monthly_interest = Decimal(input('Porcentagem de juros: '))
            period = int(input('Período de investimento: '))
            simulator = FixedInterestSimulator(
                initial_amount, monthly_interest, monthly_contribution
            )

            for i in range(1, period + 1):
                future_value = simulator.simulate(i)
                print(f'Mês: {i:02d} - Valor Total futuro: {future_value}')

            print()
        case 2:
            initial_amount = Decimal(
                input('Valor Inicial (use 0 caso não queira usar): ')
            )
            monthly_contribution = Decimal(
                input('Aportes Mensais (use 0 caso não queira usar): ')
            )
            monthly_interest = Decimal(input('Porcentagem de juros: '))
            period = int(input('Período de investimento: '))
            simulator = FixedInterestDataSimulator(
                initial_amount, monthly_interest, monthly_contribution
            )
            with open('simulation.csv', 'w') as csv_file:
                csv_output = simulator.generate_csv(period)
                csv_file.write(csv_output.getvalue())

            print('CSV gerado: simulation.csv')
            print()
        case 3:
            print('Encerrando')
        case _:
            print('Opção inválida')
            print()
