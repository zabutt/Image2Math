import streamlit as st
from PIL import Image
import pytesseract
from sympy import * 
import os

os.system("apt-get update && apt-get install -y tesseract-ocr")

def extract_problem_text(image):
    try:
        # Use Tesseract OCR to extract text from the image
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        st.error(f"Error extracting text from image: {e}")
        return None

def solve_problem(problem_text):
    try:
        # Use SymPy to parse and solve the problem
        x = symbols('x')
        expr = parse_expr(problem_text)
        solution = solve(expr, x)
        return solution
    except Exception as e:
        st.error(f"Error solving the problem: {e}")
        return None

def show_step_by_step(problem_text):
    try:
        # Use SymPy to generate step-by-step solution
        x = symbols('x')
        expr = parse_expr(problem_text)
        steps = solve(expr, x, show=True)
        return steps
    except Exception as e:
        st.error(f"Error generating step-by-step solution: {e}")
        return None

def main():
    st.title("Math Problem Solver")

    # Allow user to upload an image
    uploaded_image = st.file_uploader("Upload a math problem image", type=['jpg', 'png', 'jpeg'])

    if uploaded_image is not None:
        # Convert the uploaded image to a PIL Image object
        image = Image.open(uploaded_image)

        # Extract the problem text from the image
        problem_text = extract_problem_text(image)
        if problem_text:
            st.write("Problem text:", problem_text)

            # Give the user the option to solve or show step-by-step
            solve_or_step = st.radio("What would you like to do?", ("Solve", "Show step-by-step"))

            if solve_or_step == "Solve":
                solution = solve_problem(problem_text)
                if solution is not None:
                    st.write("Solution:", solution)
            else:
                steps = show_step_by_step(problem_text)
                if steps is not None:
                    st.write("Step-by-step solution:")
                    st.write(steps)

if __name__ == '__main__':
    main()
