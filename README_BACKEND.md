# Backend Architecture and Folder Structure

The backend of this project follows a structured layered architecture to ensure maintainability and scalability.

## Folder Structure

- `/api`

  - Contains the route definitions and API endpoint handlers.
  - Example files:
    - `product_routes.py`: Handles product-related API routes.
    - `user_routes.py`: Handles user-related API routes.

- `/services`

  - Contains the business logic related to the application's operations.
  - Example files:
    - `product_service.py`: Contains business logic for product operations.
    - `user_service.py`: Contains business logic for user operations.

- `/models`

  - Defines the data models representing the structure of the data used in the application.
  - Example files:
    - `product.py`: Data model for products.
    - `user.py`: Data model for users.

- `/repositories`

  - Handles data access operations and database queries.
  - Example files:
    - `product_repository.py`: Manages database queries for products.
    - `user_repository.py`: Manages database queries for users.

- `/utils`

  - Contains utility functions and shared components used across the application.

- `/schemas`

  - Used for data validation and serialization.

- `/core`
  - Contains core functionality and configurations essential for the application's setup and execution.

This architecture ensures separation of concerns, thereby making the application easier to manage and extend in the future.
