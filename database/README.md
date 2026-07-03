# Database Documentation

This directory contains documentation related to the database architecture used in BunnyBot.

---

## Overview

BunnyBot uses SQLite as a lightweight embedded relational database for persistent storage.

The database enables:

- Multi-user account management
- Secure login system
- User profile storage
- Conversation history
- Translation history
- Personalized interaction records

Each registered user has an independent interaction history associated with their mobile number.

---

## Database Tables

### Users

Stores user profile information.

| Field |
|-------|
| Mobile Number |
| First Name |
| Last Name |
| Birth Date |
| Gender |
| Country |
| Email |
| Password |

---

### Conversation

Stores conversations between the user and the AI assistant.

| Field |
|-------|
| ID |
| User Query |
| Assistant Response |
| Mobile Number |

---

### Translation History

Stores translation records.

| Field |
|-------|
| Source Text |
| Source Language |
| Target Text |
| Target Language |
| Mobile Number |

---

## Privacy Notice

For privacy reasons, all personal information in the database is not real, and no real user information is contained in this repository.
