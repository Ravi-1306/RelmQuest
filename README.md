# RelmQuest

A Flask-based web application for managing a role-playing game world with character creation, location tracking, and real-time chat functionality using WebSockets.

## Overview

RelmQuest is a full-stack RPG management platform that combines traditional role-playing game elements with modern web technologies. Players can create accounts, build customized characters, explore an interactive world map, and communicate with other players in real-time through location-based chat rooms.

## Key Features

- **Account Management**: Secure user registration and authentication with bcrypt password hashing
- **Character System**: Create characters with customizable races, classes, stats, and portraits
- **Character Progression**: Experience-based leveling system with stat improvements
- **Interactive World**: Navigate through countries, cities, and locations with visual maps
- **Real-Time Chat**: WebSocket-powered location-specific chat rooms with user presence tracking
- **Inventory System**: Manage character items and equipment
- **Game Content**: Pre-defined races, classes, abilities, and items with CSV import support

## Technology Stack

### Backend
- **Flask 3.0.0**: Web application framework for routing and request handling
- **Flask-SocketIO 5.3.6**: WebSocket support for real-time bidirectional communication
- **SQLAlchemy 2.0.23**: ORM for database operations and query building
- **Flask-SQLAlchemy 3.1.1**: SQLAlchemy integration with Flask
- **Flask-Bcrypt 1.0.1**: Secure password hashing
- **Flask-Reuploaded 1.4.0**: File upload management for character portraits

### Database
- **PostgreSQL** (Production): Relational database with UUID support via psycopg2
- **SQLite** (Development): File-based database with automatic fallback
- Custom GUID implementation for cross-database UUID compatibility

### Real-Time & Async
- **python-socketio 5.10.0**: Socket.IO protocol implementation
- **gevent 23.9.1**: Coroutine-based networking for async operations
- **simple-websocket 1.0.0**: WebSocket protocol support

### Additional Tools
- **Pillow 10.1.0**: Image processing for character portraits
- **python-dotenv 1.0.0**: Environment variable management
- **Jinja2 3.1.2**: Template engine for HTML rendering
- **pytest 7.4.3**: Testing framework for unit and E2E tests

## Project Structure

```
RelmQuest-main/
├── app.py                   # Main Flask application with routes and WebSocket handlers
├── init_db.py               # Database initialization script
├── requirements.txt         # Python dependencies
├── .env                     # Environment configuration
├── src/
│   ├── models.py            # SQLAlchemy ORM models
│   └── db_actions.py        # Database query functions
├── static/
│   ├── assets/              # Images and character portraits
│   └── import_csv/          # Game data CSV files
├── templates/               # Jinja2 HTML templates
└── test/                    # Unit and E2E tests
```

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment** (optional for SQLite):
   ```bash
   cp Sample.env .env
   # Edit .env with PostgreSQL credentials or leave empty for SQLite
   ```

3. **Initialize database**:
   ```bash
   python init_db.py
   ```

4. **Run application**:
   ```bash
   flask --app app.py run --debug
   ```

5. **Access**: Open http://127.0.0.1:5000 in your browser

## Configuration

### Environment Variables (.env)
```env
DB_USER=              # Leave empty for SQLite
DB_PASS=
DB_HOST=
DB_PORT=
Location=LOCAL        # LOCAL or DEPLOYMENT
APP_SECRET_KEY=dev-secret-key-change-in-production
```

### Database Selection
- **SQLite**: Automatic when PostgreSQL credentials are empty (perfect for development)
- **PostgreSQL**: Used when valid credentials provided (recommended for production)

## Key Endpoints

- `GET /` - Home page
- `GET/POST /Login` - User authentication
- `GET/POST /CreateAccount` - User registration
- `GET /Character` - Character sheet
- `GET /WorldMap` - Interactive world map
- `GET /Chat/<city_name>` - City chat room

## WebSocket Events

### Client → Server
- `connection(city_name)` - Join city chat room
- `message_sent(message, city)` - Send chat message
- `disconnect` - Leave all rooms

### Server → Client
- `chat(message, id, name, image, timestamp)` - New message
- `new_connection(name, image)` - User joined
- `disconnection(name)` - User left

## Production Deployment

```bash
# Using Gunicorn with eventlet workers
gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:8000 app:app
```

**PostgreSQL Setup**:
1. Create database: `CREATE DATABASE realmquest;`
2. Run schema: `psql -d realmquest -f PostgreDatabaseSchema.sql`
3. Configure .env with credentials
4. Initialize: `python init_db.py`

## Development

**Import CSV data**:
```bash
python csv_import.py
```

**Run tests**:
```bash
pytest test/
```

## License

Available for educational and personal use.
