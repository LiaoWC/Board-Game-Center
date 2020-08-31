var flip = 0; // 1 0 變換

$(document).ready(function choose_picture() {
    flip = $(".category_to_rating_picture").attr("name");
    var picSrc = "/static/IMG/category_to_rating_pictures/category_to_rating_" + String(flip) + ".png";
    $(".category_to_rating_picture").attr("src", picSrc);
    /*if (flip == '0') {
        $(".category_to_rating_picture").attr("src", "/static/IMG/category_to_rating_1.png");
        //flip = '1;
    }*/
    //else {
    //        $(".category_to_rating_picture").attr("src", "/static/IMG/category_to_rating_2.png");
    //flip = 0;
    //}
    // alert(flip);
})


// {
//     { url_for('static', filename = 'IMG/category_to_rating.png') }
// }