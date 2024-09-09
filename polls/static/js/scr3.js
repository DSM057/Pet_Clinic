
document.addEventListener("DOMContentLoaded", function () {
  // Восстанавливаем данные при загрузке страницы
  restoreFormData();
  // Восстанавливаем комментарии при загрузке страницы
  restoreComments();
  // Восстанавливаем прокрутку страницы
  restoreScrollPosition();
});

// Используем пустой массив в качестве начального значения переменной comments
var comments = [];

function addComment() {
  var name = document.getElementById("name-input").value;
  var service = document.getElementById("service-input").value;
  var commentText = document.getElementById("comment-input").value;

  if (name && service && commentText) {
    var comment = {
      name: name,
      service: service,
      text: commentText,
      timestamp: new Date().toLocaleString(),
    };

    comments.push(comment);

    // Сохраняем комментарии в локальном хранилище
    saveComments();

    // Обновляем отображение комментариев
    displayComments();

    // Очищаем форму
    document.getElementById("name-input").value = "";
    document.getElementById("service-input").value = "";
    document.getElementById("comment-input").value = "";
  }
}

function displayComments() {
  var commentsList = document.getElementById("comments-list");
  commentsList.innerHTML = ""; // Очищаем предыдущие комментарии

  comments.forEach(function (comment) {
    var li = document.createElement("li");
    if (comment.timestamp) {
      li.innerHTML = <strong>${comment.name}</strong> (${comment.service}): ${comment.text} - ${comment.timestamp};
    } else {
      li.innerHTML = <strong>${comment.name}</strong> (${comment.service}): ${comment.text};
    }
    commentsList.appendChild(li);
  });
}

function saveComments() {
  // Преобразуем массив комментариев в строку и сохраняем в локальном хранилище
  localStorage.setItem("comments", JSON.stringify(comments));
}

function restoreComments() {
  // Получаем комментарии из локального хранилища
  var storedComments = localStorage.getItem("comments");

  // Если комментарии найдены, парсим их обратно в массив
  if (storedComments) {
    comments = JSON.parse(storedComments);
    displayComments();
  }
}

function saveFormData() {
  // Сохраняем данные из формы в сессионное хранилище
  sessionStorage.setItem("formData", JSON.stringify(getFormData()));
}

function restoreFormData() {
  // Получаем данные из сессионного хранилища
  var storedFormData = sessionStorage.getItem("formData");

  // Если данные найдены, восстанавливаем их в форме
  if (storedFormData) {
    setFormData(JSON.parse(storedFormData));
  }

  // Добавляем обработчики событий на поля ввода для сохранения данных при изменении
  var formFields = document.querySelectorAll("input, textarea");
  formFields.forEach(function (field) {
    field.addEventListener("input", saveFormData);
  });
}

function getFormData() {
  // Получаем данные из полей формы
  var formData = {};
  formData.name = document.getElementById("name-input").value;
  formData.service = document.getElementById("service-input").value;
  formData.comment = document.getElementById("comment-input").value;
  return formData;
}

function setFormData(formData) {
  // Устанавливаем данные в поля формы
  document.getElementById("name-input").value = formData.name  "";
  document.getElementById("service-input").value = formData.service  "";
  document.getElementById("comment-input").value = formData.comment  "";
}

// Сохранение прокрутки страницы
function saveScrollPosition() {
  var scrollPosition = window.scrollY  window.pageYOffset;
  localStorage.setItem("scrollPosition", scrollPosition);
}

// Восстановление прокрутки страницы
function restoreScrollPosition() {
  var storedScrollPosition = localStorage.getItem("scrollPosition");
  if (storedScrollPosition) {
    window.scrollTo(0, storedScrollPosition);
  }
}

// Удаление данных о прокрутке, если они соответствуют концу страницы
window.addEventListener("beforeunload", function () {
  // Удаление данных о прокрутке, якщо вони відповідають кінцю сторінки
  var pageHeight = document.documentElement.scrollHeight;
  if (window.scrollY + window.innerHeight === pageHeight) {
    localStorage.removeItem("scrollPosition");
  } else {
    saveScrollPosition();
  }

  // Зберігаємо прокрутку при закритті сторінки
  saveScrollPosition();
});