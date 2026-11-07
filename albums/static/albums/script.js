
function validateAlbumForm() {

    let albumName = document.getElementById("album_name").value;
    let artist = document.getElementById("artist").value;
    let genre = document.getElementById("genre").value;
    let year = document.getElementById("year").value;

    if (albumName == "" || artist == "" ||
        genre == "" || year == "") {

        alert("Please fill all fields!");

        return false;
    }

    return true;
}
