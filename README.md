# Property Management API

This is a FastAPI-based web application for managing properties. It provides a set of APIs for creating, updating, and fetching property details.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- MongoDB

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/senthiltechspot/inviz.git
   cd inviz
   ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    Create a .env file in the root directory.

    Define the MongoDB connection URI in the .env file:

    ```bash
    MONGODB_URI="mongodb://localhost:27017"
    ```
4. Run the application:

    ```bash
    uvicorn main:app --reload
    ```

# APIs

The APIs are defined in the `routers` folder.
## APIs

### Create New Property

**Endpoint:** POST /create_new_property

**Input:**
```json
{
    "name": "Property Name",
    "address": "123 Street",
    "city": "City Name",
    "state": "State Name"
}

```

**Output:**

```json
[
    {
        "id": "property_id",
        "name": "Property Name",
        "address": "123 Street",
        "city": "City Name",
        "state": "State Name"
    }
]

```

### Fetch Property Details

**Endpoint:** GET /fetch_property_details?city=City Name

**Output:**
```json
[
    {
        "id": "property_id",
        "name": "Property Name",
        "address": "123 Street",
        "city": "City Name",
        "state": "State Name"
    }
]

```
### Update Property Details

**Endpoint:** PUT /update_property_details

**Input:**
```json
{
    "property_id": "property_id",
    "name": "Updated Property Name",
    "address": "456 New Street",
    "city": "New City Name",
    "state": "New State Name"
}

```
**Output:**
```json
[
    {
        "id": "property_id",
        "name": "Updated Property Name",
        "address": "456 New Street",
        "city": "New City Name",
        "state": "New State Name"
    }
]
```

### Find Cities by State

**Endpoint:** GET /find_cities_by_state?state=State Name

**Output:**
```json
[
    "City 1",
    "City 2",
    ...
]
```
### Find Similar Properties

**Endpoint:** GET /find_similar_properties?property_id=property_id

**Output:**
```json
[
    {
        "id": "property_id",
        "name": "Property Name",
        "address": "123 Street",
        "city": "City Name",
        "state": "State Name"
    },
    ...
]
```

## Usage

To use the APIs, refer to the [API documentation](https://github.com/senthiltechspot/inviz)

This README provides instructions on how to set up the application, run it, and use its APIs, along with examples of the input and output formats for each API endpoint.