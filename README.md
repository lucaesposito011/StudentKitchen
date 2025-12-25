# StudentKitchen

StudentKitchen is a web application developed for the Web Technologies exam at the University of Naples Parthenope.

The project was designed to support students living away from home who may have difficulties in meal preparation.
Its goal is to help them easily find recipes using the ingredients they already have, reducing food waste and encouraging healthier eating habits.

## Features
StudentKitchen provides several features designed to help students manage meal preparation in a simple and efficient way:

**User Authentication**: Users can register, log in, and log out. 

**Reverse Recipe Search**: The core feature of the application allows users to search for recipes by selecting the ingredients they already have. The system returns all recipes that include at least one of the selected ingredients, helping reduce food waste, excessive use of food delivery and waste of money.

**Recipe Details**: Each recipe includes detailed information such as ingredients, preparation steps, estimated preparation time, calorie count, and an image.

**Favorites Management**: Users can save recipes to their personal favorites list.  A dedicated page allows users to easily access all their saved recipes.

**Recipe Reviews**: Users can leave reviews and ratings for each recipe.
All reviews are displayed on the recipe detail page, allowing users to share feedback and opinions.

## Technologies Used:
**Frontend**: HTML, CSS, JavaScript

**Backend**: Python, MongoDB

**Containerization**: Docker

## How to run the web application

To run StudentKitchen, you must have installed in your pc **Docker Desktop**

**Step 1**: Clone the project repository

**Step 2**: Navigate to the project directory
```bash
    cd repository-folder
```

**Step 3**: Start the application using Docker Compose
```bash
    docker-compose up --build
```
**Step 4**: Open your favourite browser and navigate to http://localhost:5001