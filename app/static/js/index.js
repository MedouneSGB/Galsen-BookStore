
document.addEventListener('DOMContentLoaded', function() {
        var toggleNavButton = document.getElementById('toggle');
        var nav = document.querySelector('nav');

        // Cacher la nav initialement
        nav.style.display = 'none';

        // Ajouter un gestionnaire d'événements au bouton pour afficher/cacher la nav
        toggleNavButton.addEventListener('click', function() {

            if (nav.style.display === 'none') {
            nav.style.display = 'block';
          } else {
            nav.style.display = 'none';
          }
        });

        document.addEventListener('click', function(event) {
        var isClickInsideNav = nav.contains(event.target);
        var isClickInsideToggle = toggleNavButton.contains(event.target);
        if (!isClickInsideNav && !isClickInsideToggle) {
          closeNav();
        }
      });

        function closeNav() {
        nav.style.display = 'none';
      }


      });


const cardDivs = document.querySelectorAll('.element .card div');
cardDivs.forEach(div => {
  div.addEventListener('mouseenter', () => {
    div.style.backgroundColor = '#282828';
  });

  div.addEventListener('mouseleave', () => {
    div.style.backgroundColor = '#F9BF21';
    div.style.color = 'white'
  });
});

