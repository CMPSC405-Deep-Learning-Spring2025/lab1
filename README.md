# Lab 1: Implementing a Simple Neural Network

## Summary

This lab is designed to help you understand and apply the basic concepts of neural networks by implementing a simple neural network from scratch. By completing this assignment, you will gain hands-on experience in:

- Using Python to build and train a neural network with minimal external libraries.
- Connecting mathematical concepts (e.g., weighted sums, activation functions) to their implementation in code.
- Understanding and explaining the logic behind your code, reinforcing a deeper comprehension of the neural network's functionality.

## Tasks

You will implement a simple neural network for an application of your choice in Python. You are not allowed any external libraries except for NumPy for mathematical operations. You are allowed to use Python's built-in modules such as `csv` to read your data file. Choose a real-world prediction task that interests you (e.g., classifying music genres, predicting workout performance, or identifying weather patterns). You are required to:

- Define your application and the specific prediction task.
- Identify at least three input features relevant to your application.
- Find or create a small dataset to test your implementation. Ensure that your dataset contains at least 6-8 data points with a mix of labels (e.g., 0 and 1 for binary classification). Save your dataset in `data/data.csv` file.

Your neural network must:

- Have an input layer with at least three neurons (corresponding to the features).
- Contain at least one hidden layer with at least two neurons.
- Use a single output neuron to make a prediction for your chosen application.

### Step 1: Neural Network Structure (In-Class Work)

During the lab session, you must choose a real-world prediction task that interests you and create the structure for the neural network, including the input, hidden, and output layers. This work must be included in the appropriate sections of the `writing/report.md` and be committed before the end of the lab session.

### Step 2: Feed-forward

Implement the forward pass using a weighted sum and an activation function of your choice.

### Step 3: Backpropagation

Implement the backpropagation algorithm to update weights and biases.

Use Mean Squared Error (MSE) as the loss function.

### Step 4: Training Loop

Train your neural network on your dataset for a minimum of 1000 iterations. Print the loss after every 100 iterations to monitor the learning process.

### Step 5: Evaluation

Write a function to evaluate the model's accuracy on the dataset. Test your network with new data points to see if it correctly predicts outcomes.

### Step 6: Code Explanation

Write detailed comments in your code explaining each part of your implementation. Additionally, include a section in the `writing/report.md` where you explain the logic and reasoning behind each major section of your code (e.g., forward pass, backpropagation, training loop).

### Intermediate Checkpoints

Commit your code to GitHub at the following checkpoints:
- After defining the neural network structure.
- After implementing the forward pass.
- After implementing backpropagation.
- After completing the training loop.
- After evaluating the model.

### Report

Finish the report, following given prompts.

## Deliverables

Submit the following:

1. A Python script (`src/neuralnetwork.py`) containing:

- Neural network implementation (forward pass, backpropagation, and training loop).
- Comments explaining each part of your code.

2. A report (`writing/report.md`) explaining:

- Your chosen application and the neural network structure (i.e., the prediction task, features, and dataset).
- How backpropagation works in your implementation.
- A screenshot or log file showing the training loss over iterations.
- Test results demonstrating the network's performance on unseen data points.
- Detailed explanations of the logic and reasoning behind each major section of your code.

3. Dataset (`src/data/data.csv`).

4. GitHub repository with commits at the specified checkpoints.

## Evaluation Criteria

This assignment uses contract-based grading. To receive `A` for the lab, you must:

- Define a clear and feasible application submitted by 4pm on January 21st.
- Implement a functional neural network with forward pass and backpropagation using class and functions.
- Train and evaluate the model with your chosen dataset.
- Provide clear explanations of your application and backpropagation process.
- Submit detailed code explanations and intermediate commits on GitHub.

For each component that is largely incomplete or incorrect, the assignment will receive a letter grade reduction.

GatorGrader is used to assess some of the criteria above. The following will be checked by the GatorGrader tool:

1. **Source File Checks**:
    - Ensure that `neuralnetwork.py` file exists in the `src/` directory.
    - Complete all TODOs and remove the TODO markers in the `neuralnetwork.py`.
    - Ensure the file contains at least one function definition.
    - Ensure the file contains at least one class definition.

2. **Technical Writing Checks**:
    - Ensure that `report.md` file exists in the `writing/` directory.
    - Write a minimum number of meaningful words (300) in the report.
    - Complete all TODOs and remove the TODO markers in the `report.md`.
    - Ensure the report contains at least one image or screenshot.

3. **Dataset File Check**:
    - Ensure that `data.csv` file exists in the `src/data/` directory.

4. **GitHub Repository Checks**:
    - Have at least a specific minimum number of commits (6) in the repository.

### Tips for Success

Break the problem into small steps and test each part of your code as you go.

Use print statements to debug your implementation and understand what is happening at each stage.

Collaborate with classmates to discuss concepts, but ensure all code and explanations are your own.

Good luck, and have fun exploring simple neural networks!

