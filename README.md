# Auth0 clone

## **Summary:**

- **Motivation**: Our project aims to create a dedicated organization-level authentication service, empowering us with full control over user authentication and authorization. This initiative allows us to reduce dependency on third-party, paid authentication providers.
- **Authentication Method**: We will implement drf token based authentication to enhance security and flexibility in our service.

## Overview of Architecture:

### Tech Stack Used

- Django `django`
- Django Rest Framework `rest_framework` *(For creating application endpoints)*
- DJ Rest Auth `dj_rest_auth` and `dj_rest_auth.registration` *(For creating authentication endpoints*)
- DJ AllAuth `allauth` and `allauth.account` *(For enabling standard registration of dj-rest-auth (dependency))*

### Features

Authentication

- Login/Logout
- SignUp with email verification
- Password Reset with email verification

Authorization

- User level resource access restrictions.

### Architecture Diagram
![Technical Diagrams](https://github.com/VinodKW/auth0-clone/assets/40213599/7e3b651d-814f-4b2b-ace4-a1f18eb1f43f)

## Breakdown of phases of project (e.g. building backend e.g.):

### phase 1: Authentication Setup with Email Verification ( 6 hours )

- Objective
    - Establish the core authentication functinality
- Tasks
    - Set up django project
    - Implement a user model with email and password field
    - Create token authorization
    - Build API endopints for user registration, login and, logout.
    - Implement basic error handling and validation.
- Outcome
    - At the end of phase 1, we will have a functional authentication system that allows users to register, login and logout using token authentication with email verification.

### phase 2: Password Reset ( 2 hours )

- Obective
    - Establish password reset functionality.
- Tasks
    - Add password reset functionality with email verification.
- Outcome
    - Phase 2 builds upon Phase 1, adding password reset functionality to enhance user convenience.
