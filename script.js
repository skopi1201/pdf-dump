const pdfFiles = [
];


const fileList = document.getElementById('fileList');
const searchInput = document.getElementById('searchInput');
const pdfFolder = 'pdfs/';

function displayFiles(files) {
    fileList.innerHTML = '';
    files.forEach(file => {
        const li = document.createElement('li');
        const link = document.createElement('a');
        link.href = pdfFolder + file;
        link.textContent = file;
        link.target = '_blank';
        li.appendChild(link);
        fileList.appendChild(li);
    });
}

displayFiles(pdfFiles);

searchInput.addEventListener('input', () => {
    const searchTerm = searchInput.value.toLowerCase();
    const filtered = pdfFiles.filter(file => file.toLowerCase().includes(searchTerm));
    displayFiles(filtered);
});
