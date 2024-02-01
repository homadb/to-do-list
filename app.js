document.addEventListener("DOMContentLoaded", function () {
    const taskForm = document.getElementById("taskForm");
    const taskInput = document.getElementById("taskInput");
    const reminderInput = document.getElementById("reminderInput");
    const taskList = document.getElementById("taskList");

    taskForm.addEventListener("submit", function (e) {
        e.preventDefault();
        addTask();
    });

    function addTask() {
        const taskText = taskInput.value.trim();
        const reminderDateTime = reminderInput.value.trim();

        if (taskText === "") return;

        const li = document.createElement("li");
        li.innerHTML = `
            <span>${taskText}</span>
            <span>${reminderDateTime}</span>
            <button class="delete-btn" onclick="deleteTask(this)">Delete</button>
        `;
        taskList.appendChild(li);

        // Clear input fields
        taskInput.value = "";
        reminderInput.value = "";
    }

    window.deleteTask = function (element) {
        const li = element.parentElement;
        li.remove();
    };
});
