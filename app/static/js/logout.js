const allLinks = document.querySelectorAll(".tabs a");
const allTabs = document.querySelectorAll(".tab-content");
const tabContentWrapper = document.querySelector(".tab-content-wrapper");
const select = document.querySelector(".tabs-select");

const shiftTabs = (linkId) => {
  allTabs.forEach((tab, i) => {
    if (tab.id.includes(linkId)) {
      allTabs.forEach((tabItem) => {
        const height = tabContentWrapper.clientHeight;
        tabItem.style = `transform: translateY(-${i * height}px);`;
        select.value = linkId;
      });
    }
  });
};

const handleLinkChange = (elem) => {
  const linkId = elem.id;
  const hrefLinkClick = elem.href;

  allLinks.forEach((link, i) => {
    if (link.href == hrefLinkClick) {
      link.classList.add("active");
    } else {
      link.classList.remove("active");
    }
  });

  shiftTabs(linkId);
};

allLinks.forEach((elem) => {
  elem.addEventListener("click", function () {
    handleLinkChange(elem);
  });
});

//? handle proper selection for initial load
const currentHash = window.location.hash;

let activeLink = document.querySelector(`.tabs a`);

if (currentHash) {
  const visibleHash = document.getElementById(
    `${currentHash.replace("#", "")}`
  );

  if (visibleHash) {
    activeLink = visibleHash;
  }
}

activeLink.classList.toggle("active");

shiftTabs(activeLink.id);

const tabsSelect = document.querySelector(".tabs-select");

tabsSelect.addEventListener("change", function (e) {
  window.location.hash = e.target.value;
  const linkId = e.target.value;
  const elem = document.getElementById(linkId);
  handleLinkChange(elem);
});