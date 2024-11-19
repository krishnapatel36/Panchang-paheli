import streamlit as st
from pentominoes import ALL_PARTS as ALL_PARTS_1
from pentominoes_level3 import ALL_PARTS as ALL_PARTS_3
from polymino import generate_all, Grid, PENTOMINOES, solutions_svg, unique_grids
from dlx import DLX

st.title("Panchang Paheli")
st.markdown("""
<style>
    body {
        background-color: #282a36;
        color: #f8f8f2;
    }
</style>
""", unsafe_allow_html=True)
# Dropdown menu to select the level
level = st.selectbox("Select Level", ["Date Puzzle", "Date-Day-Month Puzzle"])

# Function to handle level 1
def level1():

    def sortkey(x):
        x = str(x)
        return (len(x), x)

    COLOURS = dict(I="#FFFFF0", F="#FFFFF0", L="#FFFFF0",
                P="#FFFFF0", N="#FFFFF0", T="#FFFFF0",
                U="#FFFFF0", V="#FFFFF0", W="#FFFFF0",
                X="#FFFFF0", Y="#FFFFF0", Z="#FFFFF0")

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

        solutions_svg([all_solutions[0]], filename='first_solution.svg',date_number=number,date_position=(row,column),month_name='',month_position=(0,0),day_name='',day_position=(0,0),level=1,columns=7, colour=COLOURS.get)
        svg_content = open("first_solution.svg", "r").read()
        st.image(svg_content, width=2000)
    else:
        st.write("Enter valid number between 1-31")
def level3():

    def sortkey(x):
        x = str(x)
        return (len(x), x)

    COLOURS = dict(I="#FFFFF0", F="#FFFFF0", L="#FFFFF0",
                P="#FFFFF0", N="#FFFFF0", T="#FFFFF0",
                U="#FFFFF0", V="#FFFFF0", W="#FFFFF0",
                X="#FFFFF0", Y="#FFFFF0", Z="#FFFFF0")
                
    date=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    number2 = st.selectbox("Select Date",date)
    number2=int(number2)

    month_map = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
        'May': 5, 'Jun': 6, 'Jul': 8, 'Aug': 9,
        'Sep': 10, 'Oct': 11, 'Nov': 12, 'Dec': 13
    }

    months = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]


    days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    day_map = {
        'Mon': (6,3), 'Tue': (6,4),  'Wed': (6,5), 'Thu': (6,6),
        'Fri': (7,4), 'Sat': (7,5), 'Sun': (7,6)
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
                    
                solutions_svg(all_solutions, filename='first_solution.svg',date_number=number2,date_position=(row,column),month_name=month_input1,month_position=(m_row,m_column),day_name=day_input,day_position=day_number2,level=3,columns=7, colour=COLOURS.get)
                svg_content = open("first_solution.svg", "r").read()
                st.write(f"Solution for : {number2} {month_input1} {day_input}")
                st.image(svg_content, width=2000)
            else:
                st.write("Enter valid infomation")
        else:
                st.write("Enter valid infomation")
    else:
                st.write("Enter valid infomation")
    
if level == "Date Puzzle":
    level1()
elif level == "Date-Day-Month Puzzle":
    level3()
