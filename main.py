import streamlit as st
from pentominoes import ALL_PARTS as ALL_PARTS_1
from pentominoes_level2 import ALL_PARTS as ALL_PARTS_2
from pentominoes_level3 import ALL_PARTS as ALL_PARTS_3
from polymino import generate_all, Grid, PENTOMINOES, solutions_svg, unique_grids
from dlx import DLX

st.title("Panchang Paheli")

# Dropdown menu to select the level
level = st.selectbox("Select Level", ["Level 1", "Level 2", "Level 3"])

# Function to handle level 1
def level1():

    def sortkey(x):
        x = str(x)
        return (len(x), x)

    COLOURS = dict(I="#EEAAAA", F="#DDBB99", L="#CCCC88",
                P="#BBDD99", N="#AAEEAA", T="#99DDBB",
                U="#88CCCC", V="#99BBDD", W="#AAAAEE",
                X="#BB99DD", Y="#CC88CC", Z="#DD99BB")

    date=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    number = st.selectbox("Select Date",date)
    number=int(number)
    st.write(f"Solution of date :{number}")
    if number in (29,30,31,32): 
        if number == 29:
            number = 33
        elif number == 30:
            number = 34
        elif number == 31:
            number = 35
    if number in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,33,34,35):
        row = (number - 1) // 7
        column = (number - 1) % 7
        GRID = Grid((5, 7), holes=[(4, 0), (4, 1), (4, 2), (4, 3), (row, column)])
        all_solutions = []  
        for PENTOMINOES in ALL_PARTS_1:
            POLYMINOES = generate_all(PENTOMINOES, GRID)
            POLYMINOES = [polymino.aslist for polymino in POLYMINOES]

            LABELS = list(set([element for polymino in POLYMINOES for element in polymino]))
            LABELS = sorted(LABELS, key=sortkey)
            COVER = DLX(LABELS, POLYMINOES)

            SOLUTIONS = []
            first_solution = True

            for i, SOLUTION in enumerate(COVER.generate_solutions()):
                solution_grid = Grid.from_DLX(SOLUTION)
                if not first_solution:
                    solution_grid.flip()
                SOLUTIONS.append(solution_grid)
                if first_solution:
                    first_solution = False
                    break  

            DISTINCT_SOLUTIONS = unique_grids(SOLUTIONS)
            all_solutions.extend(DISTINCT_SOLUTIONS)  

        solutions_svg([all_solutions[0]], filename='first_solution.svg',date_number=number,date_position=(row,column),level=1,columns=7, colour=COLOURS.get)
        svg_content = open("first_solution.svg", "r").read()
        st.image(svg_content, width=2000)
    else:
        st.write("Enter valid number between 1-31")

# Function to handle level 2
def level2():

    def sortkey(x):
        x = str(x)
        return (len(x), x)


    COLOURS = dict(I="#EEAAAA", F="#DDBB99", L="#CCCC88",
                P="#BBDD99", N="#AAEEAA", T="#99DDBB",
                U="#88CCCC", V="#99BBDD", W="#AAAAEE",
                X="#BB99DD", Y="#CC88CC", Z="#DD99BB")

    date=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    number1 = st.selectbox("Select Date",date)
    number1=int(number1)

    month_map = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 8, 'August': 9,
        'September': 10, 'October': 11, 'November': 12, 'December': 13
    }
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    # Dropdown for selecting a month
    month_input = st.selectbox("Select Month:", months)
    if number1 in range(1,32):
        if month_input in months:
            month_number1 = month_map[month_input]
            m_row = (month_number1 - 1) // 7
            m_column = (month_number1 - 1) % 7

            row = (number1 - 1) // 7 + 2
            column = (number1 - 1) % 7

            GRID = Grid((7, 7), holes=[(0, 6), (1, 6), (6, 3), (6, 4), (6, 5), (6, 6), (row, column), (m_row, m_column)])

            all_solutions = []
            for PENTOMINOES in ALL_PARTS_2:
                POLYMINOES = generate_all(PENTOMINOES, GRID)
                POLYMINOES = [polymino.aslist for polymino in POLYMINOES]

                LABELS = list(set([element for polymino in POLYMINOES for element in polymino]))
                LABELS = sorted(LABELS, key=sortkey)
                COVER = DLX(LABELS, POLYMINOES)

                SOLUTIONS = []
                first_solution = True

                for i, SOLUTION in enumerate(COVER.generate_solutions()):
                    solution_grid = Grid.from_DLX(SOLUTION)
                    if not first_solution:
                        solution_grid.flip()
                    SOLUTIONS.append(solution_grid)
                    if first_solution:
                        first_solution = False
                        break

                DISTINCT_SOLUTIONS = unique_grids(SOLUTIONS)
                all_solutions.extend(DISTINCT_SOLUTIONS)
            solutions_svg(all_solutions, filename='first_solution.svg', columns=1, colour=COLOURS.get)
            svg_content = open("first_solution.svg", "r").read()
            st.write(f"Solution for : {number1} {month_input}")
            st.image(svg_content, width=300)

        else:
            st.write("Enter Valid Info")
    else:
            st.write("Enter Valid Info")
    
# Function to handle level 3
def level3():

    def sortkey(x):
        x = str(x)
        return (len(x), x)

    COLOURS = dict(I="#EEAAAA", F="#DDBB99", L="#CCCC88",
                P="#BBDD99", N="#AAEEAA", T="#99DDBB",
                U="#88CCCC", V="#99BBDD", W="#AAAAEE",
                X="#BB99DD", Y="#CC88CC", Z="#DD99BB")

    date=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    number2 = st.selectbox("Select Date",date)
    number2=int(number2)

    month_map = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 8, 'August': 9,
        'September': 10, 'October': 11, 'November': 12, 'December': 13
    }

    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]


    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    day_map = {
        'Monday': (6,3), 'Tuesday': (6,4),  'Wednesday': (6,5), 'Thursday': (6,6),
        'Friday': (7,4), 'Saturday': (7,5), 'Sunday': (7,6)
    }

    # Get user input for the month
    month_input1 = st.selectbox("Select Month:", months)
    day_input = st.selectbox("Select Day",days)

    if number2 in range(1,32):
        if month_input1 in months:
            if day_input in days:
                month_number2 = month_map[month_input1]
                day_number2 = day_map[day_input]
                m_row = (month_number2 - 1) // 7
                m_column=(month_number2 - 1) % 7 

                row = (number2 - 1) // 7 + 2
                column=(number2 - 1) % 7

                GRID = Grid((8, 7), holes=[(0, 6), (1, 6),(7, 0),(7, 1),(7, 2),(7, 3),(row, column),(m_row, m_column),day_number2])

                all_solutions = []
                for PENTOMINOES in ALL_PARTS_3:
                    POLYMINOES = generate_all(PENTOMINOES, GRID)
                    POLYMINOES = [polymino.aslist for polymino in POLYMINOES]

                    LABELS = list(set([element for polymino in POLYMINOES for element in polymino]))
                    LABELS = sorted(LABELS, key=sortkey)
                    COVER = DLX(LABELS, POLYMINOES)

                    SOLUTIONS = []
                    first_solution = True  

                    for i, SOLUTION in enumerate(COVER.generate_solutions()):
                        solution_grid = Grid.from_DLX(SOLUTION)
                        if not first_solution:
                            solution_grid.flip()
                        SOLUTIONS.append(solution_grid)
                        if first_solution:
                            first_solution = False
                            break

                    DISTINCT_SOLUTIONS = unique_grids(SOLUTIONS)
                    all_solutions.extend(DISTINCT_SOLUTIONS)
                    
                solutions_svg(all_solutions, filename='first_solution.svg', columns=7, colour=COLOURS.get)
                svg_content = open("first_solution.svg", "r").read()
                st.write(f"Solution for : {number2} {month_input1} {day_input}")
                st.image(svg_content, width=2000)
            else:
                st.write("Enter valid infomation")
        else:
                st.write("Enter valid infomation")
    else:
                st.write("Enter valid infomation")
    
if level == "Level 1":
    level1()
elif level == "Level 2":
    level2()
elif level == "Level 3":
    level3()
