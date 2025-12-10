
-- 1. LIMPIEZA DE DATOS
-- Elimino datos de todas las tablas en orden para evitar errores de Foreign Key.
-- RESTART IDENTITY reinicia los contadores auto-incrementales a 1.
TRUNCATE TABLE
    task_tag,
    task,
    tag,
    sprint,
    programmer,
    rol_programmer,
    sprint_status,
    task_priority,
    task_status,
    usuario
    RESTART IDENTITY CASCADE;

-- 2. INSERCIÓN DE DATOS MAESTROS / AUXILIARES

-- Roles de Programador (Necesarios para crear Programadores)
INSERT INTO rol_programmer (name) VALUES
                                      ('Junior Developer'),
                                      ('Senior Developer'),
                                      ('Tech Lead'),
                                      ('QA Engineer'),
                                      ('DevOps Engineer');

-- Estados de Sprint (Necesarios para crear Sprints)
INSERT INTO sprint_status (name) VALUES
                                     ('Planning'),
                                     ('In Progress'),
                                     ('Finished'),
                                     ('Review');

-- Prioridades de Tarea
INSERT INTO task_priority (name) VALUES
                                     ('Low'),
                                     ('Medium'),
                                     ('High'),
                                     ('Critical');

-- Estados de Tarea
INSERT INTO task_status (name) VALUES
                                   ('To Do'),
                                   ('In Progress'),
                                   ('Blocked'),
                                   ('Done');

-- 3. INSERCIÓN DE DATOS PRINCIPALES

-- Programadores
INSERT INTO programmer (name, email, capacity, rol_id) VALUES
                                                           ('Ana García', 'ana.garcia@devteam.com', 5, 1),      -- Junior
                                                           ('Carlos Ruiz', 'carlos.ruiz@devteam.com', 8, 2),    -- Senior
                                                           ('Elena Martín', 'elena.martin@devteam.com', 10, 3), -- Lead
                                                           ('David López', 'david.lopez@devteam.com', 6, 4),    -- QA
                                                           ('Sofía Hernanz', 'sofia.hernanz@devteam.com', 7, 5); -- DevOps

-- Sprints

INSERT INTO sprint (name, start_date, end_date, goal, status_id) VALUES
                                                                     ('Sprint 1: Core', '2023-10-01', '2023-10-14', 'Implementación del núcleo de la aplicación y base de datos', 3), -- Finished
                                                                     ('Sprint 2: UI & Features', '2023-10-15', '2023-10-29', 'Desarrollo de interfaz de usuario y funcionalidades principales', 2); -- In Progress

-- Etiquetas / Tags
INSERT INTO tag (name) VALUES
                           ('Backend'),
                           ('Frontend'),
                           ('Database'),
                           ('API REST'),
                           ('Security'),
                           ('UI/UX'),
                           ('Bug'),
                           ('Refactoring'),
                           ('Documentation'),
                           ('Testing');

-- Tareas
-- Relacionamos con Sprints (1 y 2), Programadores (1-5), Prioridades y Estados.
INSERT INTO task (title, description, story_points, estimated_hours, spent_hours, created_at, updated_at, priority_id, status_id, sprint_id, programmer_id) VALUES
-- Tareas del Sprint 1
('Diseño de Base de Datos', 'Crear diagrama ER y scripts SQL iniciales', 5, 8, 8, NOW(), NOW(), 3, 4, 1, 3), -- Done, Lead
('Configuración Inicial Spring', 'Setup del proyecto, dependencias y estructura de carpetas', 3, 4, 4, NOW(), NOW(), 2, 4, 1, 5), -- Done, DevOps
('Implementar Entidades JPA', 'Crear clases @Entity para el modelo de datos', 5, 10, 10, NOW(), NOW(), 3, 4, 1, 1), -- Done, Junior
('Configurar Seguridad', 'Implementar Spring Security básico', 8, 16, 16, NOW(), NOW(), 4, 4, 1, 2), -- Done, Senior
('API: CRUD Usuarios', 'Endpoints para gestión de usuarios', 3, 6, 6, NOW(), NOW(), 2, 4, 1, 1), -- Done, Junior

-- Tareas del Sprint 2
('Maquetación Dashboard', 'Diseñar vista principal con HTML/CSS', 5, 10, 5, NOW(), NOW(), 2, 2, 2, 1), -- In Progress, Junior
('Integración API Tareas', 'Conectar frontend con endpoint de tareas', 5, 8, 2, NOW(), NOW(), 3, 2, 2, 2), -- In Progress, Senior
('Corrección Login Bug', 'Arreglar error al redirigir tras login fallido', 2, 4, 0, NOW(), NOW(), 4, 1, 2, 4), -- To Do, QA
('Optimización Consultas', 'Mejorar performance en listado de sprints', 3, 5, 0, NOW(), NOW(), 1, 1, 2, 3), -- To Do, Lead
('Escribir Tests Unitarios', 'Cubrir servicios principales con JUnit', 8, 12, 0, NOW(), NOW(), 2, 1, 2, 4); -- To Do, QA

-- 4. RELACIONES MUCHOS A MUCHOS
INSERT INTO task_tag (task_id, tag_id) VALUES
                                           (1, 3), (1, 1), -- Tarea 1: Database, Backend
                                           (2, 1), (2, 5), -- Tarea 2: Backend, Security
                                           (3, 1), (3, 3), -- Tarea 3: Backend, Database
                                           (4, 5), (4, 1), -- Tarea 4: Security, Backend
                                           (5, 4), (5, 1), -- Tarea 5: API REST, Backend
                                           (6, 2), (6, 6), -- Tarea 6: Frontend, UI/UX
                                           (7, 2), (7, 4), -- Tarea 7: Frontend, API REST
                                           (8, 7), (8, 6), -- Tarea 8: Bug, UI/UX
                                           (9, 8), (9, 3), -- Tarea 9: Refactoring, Database
                                           (10, 10), (10, 1); -- Tarea 10: Testing, Backend