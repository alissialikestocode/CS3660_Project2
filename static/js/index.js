async function include(element, page) {
    var contentObject = await fetch(page);
    var contentHTML = await contentObject.text();
    element.innerHTML = contentHTML;

    element.querySelectorAll("[href]").forEach(
        subelement => {
            var href = subelement.getAttribute("href");
            subelement.setAttribute("href", basedir + href);
        }
    )

    element.querySelectorAll("[src]").forEach(
        subelem => { 
            var src = subelem.getAttribute("src");
            subelem.setAttribute("src", basedir + src);
        }
    )
}

function includeall() {
    document.querySelectorAll(
        "[data-include]"
    ).forEach(
        el => include(el, el.getAttribute("data-include"))
    );
}