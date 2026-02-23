# Part 4 - Simple Web Client

## Project Overview

This project represents Part 4 of the HBnB Evolution system.  
In this phase, we implemented a simple web client that interacts with the HBnB backend API.

The objective of this part is to build a structured and functional front-end using HTML, CSS, and JavaScript, while integrating it with the existing RESTful API.

The interface dynamically communicates with the backend and renders data to users in a clean and organized layout.

---

## Objectives

- Connect the front-end to the HBnB RESTful API  
- Fetch and display dynamic data using the Fetch API  
- Implement filtering functionality  
- Handle authentication if required  
- Maintain separation between front-end and back-end  
- Follow clean and maintainable code practices  

---


## Project Structure

```
part4/
│
├── style.css
│
├── script.js
│
├── index.html
├── about.html
├── add_review.html
├── login.html
├── place.html
│
├── images/
│ └── logo.png
│
└── README.md
```


---

## Implemented Features

### Dynamic Data Fetching
- Uses JavaScript `fetch()` to retrieve data from API endpoints  
- Parses JSON responses  
- Dynamically renders content inside the DOM  

### Places Display
The interface displays:
- Place name  
- Price  
- Description  
- Location  
- Amenities (if available)  

### Filtering System
Users can filter places based on:
- Price range  
- City  
- Amenities  

### Authentication (if implemented)
- Login form  
- Token storage using LocalStorage  
- Attaching JWT token to protected requests  

---

## How to Run

1. Ensure the backend server is running.
2. Open the `index.html` file in your browser.
3. Confirm that the API base URL is correctly configured inside `script.js`.

Example:

```
const API_BASE_URL = "http://127.0.0.1:5000/api/v1";
```

## Technologies Used
- HTML5
- CSS3
- JavaScript (ES6)
- REST API
- Fetch API

---

## Project Preview :


<div align="center">
<img width="300" height="650" alt="image" src="https://github.com/user-attachments/assets/5eec15d9-1783-43a8-a6c9-c9403a6281ae" />
<img width="300" height="650" alt="image" src="https://github.com/user-attachments/assets/852d0d61-5280-45af-a79d-01b27e94eeac" />
</div>

<div align="center">
<img width="300" height="650" alt="image" src="https://github.com/user-attachments/assets/de361558-be2e-4593-8782-d1c97854da13" />
<img width="300" height="650" alt="image" src="https://github.com/user-attachments/assets/d1c49e58-4a40-48b4-896a-7fc0099a3cd1" />
</div>

---

## Future Improvements

- Improve UI/UX design
- Add pagination
- Add detailed place view page
- Improve filtering logic
- Implement booking functionality

---
## Summary

Part 4 of the HBnB Evolution project focuses on building a functional and structured web client that communicates with the backend RESTful API. 

In this phase, we implemented a dynamic front-end using HTML, CSS, and JavaScript to fetch, display, and manage data related to places and user interactions. The client ensures proper integration with the backend services while maintaining clean design, organized structure, and separation of concerns.

This part demonstrates the complete connection between front-end and back-end components, transforming the system into a fully interactive web application.
