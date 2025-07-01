import os

folder = 'pdfs'
files = [f for f in os.listdir(folder) if f.endswith('.pdf')]

with open('script.js', 'w', encoding='utf-8') as js:
    js.write("const pdfFiles = [\n")
    for f in files:
        js.write(f"    '{f}',\n")
    js.write("];\n\n")

    js.write("""
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
""")

print(f"✅ Generated script.js with {len(files)} PDF(s).")
