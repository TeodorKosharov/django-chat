const errors = document.querySelectorAll('li');
const main = document.querySelector('main');
const errorsList = document.querySelector('ul');

if (errorsList) {
    errorsList.style.display = 'none';
}

errors.forEach(err => {
    const errorParagraph = document.createElement('p');
    errorParagraph.className = 'error-paragraph';
    errorParagraph.textContent = err.textContent;

    const symbol = document.createElement('i');
    symbol.className = 'fa-solid fa-ban';
    errorParagraph.prepend(symbol);

    main.insertBefore(errorParagraph, main.children[1]);
});