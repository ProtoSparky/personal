function RunWebsite() {
  // Add content to your website here

  // Text
  document.write("Welcome to my digital garden!");

  // Image
  let image = document.createElementNS("http://www.w3.org/2000/svg", "image");
  image.setAttribute("x", "100");
  image.setAttribute("y", "100");
  image.setAttribute("width", "50");
  image.setAttribute("height", "50");
  image.setAttributeNS("http://www.w3.org/1999/xlink", "href", "https://via.placeholder.com/50");
  document.body.appendChild(image);

  // Button
  let button = document.createElement("button");
  button.innerHTML = "Click me!";
  button.onclick = function() {
    alert("Thanks for clicking!");
  };
  document.body.appendChild(button);

  // Form
  let form = document.createElement("form");
  form.action = "#";
  form.method = "get";
  form.innerHTML = `
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="message">Message:</label>
    <textarea id="message" name="message"></textarea><br><br>
    <input type="submit" value="Submit">
  `;
  document.body.appendChild(form);

  // Quiz
  let quiz = document.createElement("div");
  quiz.innerHTML = `
    <h2>Quiz</h2>
    <p>What is the capital of France?</p>
    <ol>
      <li><input type="radio" name="quiz" value="Paris"> Paris</li>
      <li><input type="radio" name="quiz" value="London"> London</li>
      <li><input type="radio" name="quiz" value="Berlin"> Berlin</li>
    </ol>
    <button id="submit-quiz">Submit</button>
  `;
  document.body.appendChild(quiz);

  // Weather Forecast
  let weatherForecast = document.createElement("div");
  weatherForecast.innerHTML = `
    <h2>Weather Forecast</h2>
    <p>Current Temperature: ${getCurrentTemperature()}°C</p>
    <p>5-day forecast:</p>
    <ul>
      ${getForecast(5).map((day) => `
        <li>${day.date}: ${day.temperature}°C</li>
      `)}
    </ul>
  `;
  document.body.appendChild(weatherForecast);

  // Calendar
  let calendar = document.createElement("div");
  calendar.innerHTML = `
    <h2>Calendar</h2>
    ${getUpcomingEvents().map((event) => `
      <p><strong>${event.title}</strong></p>
      <p>${event.description}</p>
      <p>Date: ${event.date}</p>
    `)}
  `;
  document.body.appendChild(calendar);

  // Chatbot
  let chatbot = document.createElement("div");
  chatbot.innerHTML = `
    <h2>Chatbot</h2>
    ${getGreeting()}<br><br>
    ${getHelpMessage()}
  `;
  document.body.appendChild(chatbot);

  // Podcast Player
  let podcastPlayer = document.createElement("div");
  podcastPlayer.innerHTML = `
    <h2>Podcast Player</h2>
    ${getCurrentEpisode()}<br><br>
    ${getPlaylist()}
  `;
  document.body.appendChild(podcastPlayer);

  // Game
  let game = document.createElement("div");
  game.innerHTML = `
    <h2>Game</h2>
    ${getInstructions()}<br><br>
    ${getScoreBoard()}
  `;
  document.body.appendChild(game);

  // Virtual Scrapbook
  let virtualScrapbook = document.createElement("div");
  virtualScrapbook.innerHTML = `
    <h2>Virtual Scrapbook</h2>
    ${getPhotos()}<br><br>
    ${getNotes()}
  `;
  document.body.appendChild(virtualScrapbook);

  // Weather Radar
  let weatherRadar = document.createElement("div");
  weatherRadar.innerHTML = `
    <h2>Weather Radar</h2>
    ${getCurrentWeather()}<br><br>
    ${getForecast(5).map((day) => `
      <p>${day.date}: ${day.temperature}°C</p>
    `)}
  `;
  document.body.appendChild(weatherRadar);

  // News Feed
  let newsFeed = document.createElement("div");
  newsFeed.innerHTML = `
    <h2>News Feed</h2>
    ${getLatestArticles()}<br><br>
    ${getArchiveLink()}
  `;
  document.body.appendChild(newsFeed);
}

function getCurrentTemperature() {
  return Math.floor((Math.random() * 10) + 20);
}

function getForecast(numDays) {
  let forecast = [];
  for (let i = 0; i < numDays; i++) {
    const day = {};
    day.date = new Date(Date.now() + (i * 86400000));
    day.temperature = getCurrentTemperature();
    forecast.push(day);
  }
  return forecast;
}

function getUpcomingEvents() {
  let events = [];
  for (let i = 0; i < 5; i++) {
    const event = {};
    event.title = `Event ${i + 1}`;
    event.description = `This is a description of Event ${i + 1}.`;
    event.date = new Date(Date.now() + (i * 86400000));
    events.push(event);
  }
  return events;
}

function getGreeting() {
  const greetings = [
    'Hi there!',
    'Hello, friend!',
    'Howdy!',
  ];
  return greetings[Math.floor(Math.random() * greetings.length)];
}

function getHelpMessage() {
  const helpMessages = [
    'I\'m here to help you with any questions or problems you might have.',
    'If you need assistance, just let me know!',
    'I\'m always happy to help.',
  ];
  return helpMessages[Math.floor(Math.random() * helpMessages.length)];
}

function getCurrentEpisode() {
  const episodes = [
    `We are currently listening to episode ${Math.floor(Math.random() * 10) + 1} of our podcast.`,
    'We are currently on a break and will resume soon!',
    'This is our latest episode, enjoy!',
  ];
  return episodes[Math.floor(Math.random() * episodes.length)];
}

function getPlaylist() {
  const playlist = [
    `We have ${Math.floor(Math.random() * 10) + 20} new episodes available in our podcast playlist!`,
    'Check them out and enjoy!',
    'We are constantly adding new content, come back soon!',
  ];
  return playlist[Math.floor(Math.random() * playlist.length)];
}

function getInstructions() {
  const instructions = [
    `Game Instructions: To play the game, simply click on the "Start" button and follow the
instructions provided.`,
    'To win, you must complete all the challenges and tasks within the time limit.',
    'Good luck!',
  ];
  return instructions[Math.floor(Math.random() * instructions.length)];
}

function getScoreBoard() {
  const scoreBoard = [
    `Current Score: ${Math.floor(Math.random() * 100) + 1}/5`,
    'To continue, simply click on the "Continue" button.',
    'Good luck!',
  ];
  return scoreBoard[Math.floor(Math.random() * scoreBoard.length)];
}

function getPhotos() {
  const photos = [
    `We currently have ${Math.floor(Math.random() * 10) + 20} photos in our virtual scrapbook.`,
    'You can add your own by clicking on the "Add Photo" button.',
    'Enjoy!',
  ];
  return photos[Math.floor(Math.random() * photos.length)];
}

function getNotes() {
  const notes = [
    `We currently have ${Math.floor(Math.random() * 10) + 20} notes in our virtual scrapbook.`,
    'You can add your own by clicking on the "Add Note" button.',
    'Enjoy!',
  ];
  return notes[Math.floor(Math.random() * notes.length)];
}

function getLatestArticles() {
  const articles = [
    `We currently have ${Math.floor(Math.random() * 10) + 20} latest news articles in our archive.`,
    'You can view them by clicking on the "View" button.',
    'Enjoy!',
  ];
  return articles[Math.floor(Math.random() * articles.length)];
}

function getArchiveLink() {
  const links = [
    `Want to see all our archive articles? Click on the "View Archive" link!`,
    'Enjoy!',
    'We are constantly adding new content, come back soon!',
  ];
  return links[Math.floor(Math.random() * links.length)];
}

// Create and append buttons to the page
function createButtons() {
  const buttons = [
    { name: 'Create List', id: 'create-list' },
    { name: 'Delete List', id: 'delete-list' },
    { name: 'Add Task', id: 'add-task' },
    { name: 'Delete Task', id: 'delete-task' },
    { name: 'Clear Completed', id: 'clear-completed' },
    { name: 'Sort List By Priority', id: 'sort-list-by-priority' },
  ];
  buttons.forEach((button) => {
    const buttonElement = document.createElement('button');
    buttonElement.innerHTML = button.name;
    buttonElement.setAttribute('id', button.id);
    buttonElement.classList.add('btn-primary');
    buttonElement.addEventListener('click', () => handleButtonClick(button.id));
    document.body.appendChild(buttonElement);
  });
}

// Add event listener to all list items in the page
function addEventListenersToAllItems() {
  const listItems = document.querySelectorAll('.list-item');
  listItems.forEach((listItem) => {
    listItem.addEventListener('click', (event) => handleListItemClick(event));
  });
}

// Add event listener to the "Clear Completed" button
function addEventListenerToClearCompleted() {
  const clearCompletedButton = document.getElementById('clear-completed');
  clearCompletedButton.addEventListener('click', (event) => handleClearCompletedClick(event));
}

// Add event listener to the "Sort List By Priority" button
function addEventListenerToSortListByPriority() {
  const sortListByPriorityButton = document.getElementById('sort-list-by-priority');
  sortListByPriorityButton.addEventListener('click', (event) => handleSortListByPriorityClick(event));
}

// Add event listener to the "Add Task" button
function addEventListenerToAddTask() {
  const addTaskButton = document.getElementById('add-task');
  addTaskButton.addEventListener('click', (event) => handleAddTaskClick(event));
}

// Handle a click on any list item
function handleListItemClick(event) {
  // If the item is not marked as completed, mark it as completed and vice versa
  if (!event.target.classList.contains('completed')) {
    event.target.classList.add('completed');
    event.target.children[0].checked = true;
  } else {
    event.target.classList.remove('completed');
    event.target.children[0].checked = false;
  }
}

// Handle a click on the "Clear Completed" button
function handleClearCompletedClick(event) {
  // Get all list items in the page
  const listItems = document.querySelectorAll('.list-item');
  let completedTasksCount = 0;

  // Iterate through all list items and if the item is marked as completed, remove it from the page
  listItems.forEach((listItem) => {
    if (listItem.classList.contains('completed')) {
      listItem.remove();
      completedTasksCount += 1;
    }
  });

  // Show a message that indicates how many tasks were removed from the page
  const message = `Removed ${completedTasksCount} completed task${completedTasksCount > 1 ? 's' :
''}.`;
  showMessage(message);
}

// Handle a click on the "Sort List By Priority" button
function handleSortListByPriorityClick(event) {
  // Get all list items in the page
  const listItems = document.querySelectorAll('.list-item');

  // Iterate through all list items and sort them by priority
  listItems.forEach((listItem, index) => {
    const taskPriorityInputValue = listItem.children[0].value;
    if (taskPriorityInputValue === 'high') {
      listItem.style.order = 1;
    } else if (taskPriorityInputValue === 'medium') {
      listItem.style.order = 2;
    } else if (taskPriorityInputValue === 'low') {
      listItem.style.order = 3;
    }
  });
}

// Handle a click on the "Add Task" button
function handleAddTaskClick(event) {
  // Create and append new list item to the page
  const listItem = createListItem();
  document.body.appendChild(listItem);
}

// Create and return a new list item element with all its child elements
function createListItem() {
  const listItem = document.createElement('li');
  listItem.classList.add('list-item');

  // Create and append input checkbox
  const taskPriorityInput = document.createElement('input');
  taskPriorityInput.setAttribute('type', 'checkbox');
  taskPriorityInput.setAttribute('value', 'medium');
  listItem.appendChild(taskPriorityInput);

  // Create and append text input for the task title
  const taskTitleInput = document.createElement('input');
  taskTitleInput.setAttribute('type', 'text');
  taskTitleInput.setAttribute('placeholder', 'Add Task Title...');
  listItem.appendChild(taskTitleInput);

  // Create and append button to delete the task
  const taskDeleteButton = document.createElement('button');
  taskDeleteButton.innerHTML = 'X';
  taskDeleteButton.classList.add('btn-delete');
  listItem.appendChild(taskDeleteButton);

  return listItem;
}

// Handle a click on any button that is not the "Add Task" or "Clear Completed" buttons
function handleButtonClick(buttonId) {
  if (buttonId !== 'add-task' && buttonId !== 'clear-completed') {
    showMessage(`Button with id "${buttonId}" is currently unsupported.`);
  }
}

// Show a message on the page
function showMessage(message) {
  const messageElement = document.createElement('p');
  messageElement.innerHTML = message;
  document.body.appendChild(messageElement);
  setTimeout(() => { messageElement.remove(); }, 5000);
}