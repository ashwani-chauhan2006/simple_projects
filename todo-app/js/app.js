// DOM Elements
const taskInput = document.getElementById('task-input');
const addTaskBtn = document.getElementById('add-task');
const todoList = document.getElementById('todo-list');
const filterBtns = document.querySelectorAll('.filter-btn');
const clearCompletedBtn = document.getElementById('clear-completed');
const tasksCount = document.getElementById('tasks-count');
const themeToggle = document.querySelector('.theme-toggle');

// State
let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
let currentFilter = 'all';

// Theme
const theme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', theme);
updateThemeIcon();

// Event Listeners
addTaskBtn.addEventListener('click', addTask);
taskInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') addTask();
});
clearCompletedBtn.addEventListener('click', clearCompleted);
themeToggle.addEventListener('click', toggleTheme);

// Add filter event listeners
filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = btn.dataset.filter;
        renderTasks();
    });
});

// Functions
function addTask() {
    const taskText = taskInput.value.trim();
    if (taskText) {
        const task = {
            id: Date.now(),
            text: taskText,
            completed: false
        };
        tasks.push(task);
        saveTasks();
        renderTasks();
        taskInput.value = '';
    }
}

function deleteTask(id) {
    tasks = tasks.filter(task => task.id !== id);
    saveTasks();
    renderTasks();
}

function toggleTask(id) {
    tasks = tasks.map(task => {
        if (task.id === id) {
            return { ...task, completed: !task.completed };
        }
        return task;
    });
    saveTasks();
    renderTasks();
}

function clearCompleted() {
    tasks = tasks.filter(task => !task.completed);
    saveTasks();
    renderTasks();
}

function renderTasks() {
    const filteredTasks = tasks.filter(task => {
        if (currentFilter === 'active') return !task.completed;
        if (currentFilter === 'completed') return task.completed;
        return true;
    });

    todoList.innerHTML = '';
    filteredTasks.forEach(task => {
        const li = document.createElement('li');
        li.className = 'todo-item';
        li.innerHTML = `
            <input type="checkbox" class="todo-checkbox" ${task.completed ? 'checked' : ''}>
            <span class="todo-text ${task.completed ? 'completed' : ''}">${task.text}</span>
            <button class="todo-delete">
                <i class="fas fa-trash"></i>
            </button>
        `;

        const checkbox = li.querySelector('.todo-checkbox');
        const deleteBtn = li.querySelector('.todo-delete');

        checkbox.addEventListener('change', () => toggleTask(task.id));
        deleteBtn.addEventListener('click', () => deleteTask(task.id));

        todoList.appendChild(li);
    });

    updateTasksCount();
}

function updateTasksCount() {
    const activeTasks = tasks.filter(task => !task.completed).length;
    tasksCount.textContent = `${activeTasks} ${activeTasks === 1 ? 'task' : 'tasks'} left`;
}

function saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon();
}

function updateThemeIcon() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const moonIcon = themeToggle.querySelector('.fa-moon');
    const sunIcon = themeToggle.querySelector('.fa-sun');
    
    if (currentTheme === 'light') {
        moonIcon.style.display = 'block';
        sunIcon.style.display = 'none';
    } else {
        moonIcon.style.display = 'none';
        sunIcon.style.display = 'block';
    }
}

// Initial render
renderTasks(); 