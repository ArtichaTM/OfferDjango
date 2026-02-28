$(document).ready(function(){
    $('.slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true
    });
    $('.slider-nav').slick({
        infinite: true,
        slidesToShow: 5,
        slidesToScroll: 1,
        asNavFor: '.slider',
        focusOnSelect: true,
        centerMode: true
    });
});
