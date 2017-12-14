$.getScript("/static/js/particles.js", function(){
    particlesJS('particles-js',
      {
        "particles": {
          "number": {
            "value": 80,
            "density": {
              "enable": true,
              "value_area": 800
            }
          },
          "color": {
            "value": "#ffffff"
          },
          "shape": {
            "type": "circle",
            "stroke": {
              "width": 0,
              "color": "#000000"
            },
            "polygon": {
              "nb_sides": 5
            },
            "image": {
              "width": 100,
              "height": 100
            }
          },
          "opacity": {
            "value": 0.5,
            "random": false,
            "anim": {
              "enable": false,
              "speed": 1,
              "opacity_min": 0.1,
              "sync": false
            }
          },
          "size": {
            "value": 5,
            "random": true,
            "anim": {
              "enable": false,
              "speed": 40,
              "size_min": 0.1,
              "sync": false
            }
          },
          "line_linked": {
            "enable": true,
            "distance": 150,
            "color": "#ffffff",
            "opacity": 0.4,
            "width": 1
          },
          "move": {
            "enable": true,
            "speed": 6,
            "direction": "none",
            "random": false,
            "straight": false,
            "out_mode": "out",
            "attract": {
              "enable": false,
              "rotateX": 600,
              "rotateY": 1200
            }
          }
        },
        "interactivity": {
          "detect_on": "canvas",
          "events": {
            "onhover": {
              "enable": true,
              "mode": "repulse"
            },
            "onclick": {
              "enable": true,
              "mode": "push"
            },
            "resize": true
          },
          "modes": {
            "grab": {
              "distance": 400,
              "line_linked": {
                "opacity": 1
              }
            },
            "bubble": {
              "distance": 400,
              "size": 40,
              "duration": 2,
              "opacity": 8,
              "speed": 3
            },
            "repulse": {
              "distance": 200
            },
            "push": {
              "particles_nb": 4
            },
            "remove": {
              "particles_nb": 2
            }
          }
        },
        "retina_detect": true,
        "config_demo": {
          "hide_card": false,
          "background_color": "#b61924",
          "background_image": "",
          "background_position": "50% 50%",
          "background_repeat": "no-repeat",
          "background_size": "cover"
        }
      }
    );

});

(function($) {
    'use strict';
    // Sort us out with the options parameters
    var getAnimOpts = function (a, b, c) {
            if (!a) { return {duration: 'normal'}; }
            if (!!c) { return {duration: a, easing: b, complete: c}; }
            if (!!b) { return {duration: a, complete: b}; }
            if (typeof a === 'object') { return a; }
            return { duration: a };
        },
        getUnqueuedOpts = function (opts) {
            return {
                queue: false,
                duration: opts.duration,
                easing: opts.easing
            };
        };
    // Declare our new effects
    $.fn.showDown = function (a, b, c) {
        var slideOpts = getAnimOpts(a, b, c), fadeOpts = getUnqueuedOpts(slideOpts);
        $(this).hide().css('opacity', 0).slideDown(slideOpts).animate({ opacity: 1 }, fadeOpts);
    };
    $.fn.hideUp = function (a, b, c) {
        var slideOpts = getAnimOpts(a, b, c), fadeOpts = getUnqueuedOpts(slideOpts);
        $(this).show().css('opacity', 1).slideUp(slideOpts).animate({ opacity: 0 }, fadeOpts);
    };
}(jQuery));

$(function() {
  $('#login-box').showDown(1000);
});