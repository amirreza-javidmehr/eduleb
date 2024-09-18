function content_session(slug, id) {
    $.get(`/courses/${slug}/${id}`).then(
        response => {
            const newElement = `<video width="700" height="400" controls class="video">
                                   <source src="${response['session']}" type="video/mp4">
                               </video>`;
            document.getElementById('content_session').innerHTML = newElement;
        }
    );
}

const form = document.getElementById('comment-form');
const slug = window.location.pathname
form.addEventListener('submit',submitHandle);
function submitHandle(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url: `http://localhost:8000${slug}add-comment/`,
        data: $('#comment-form').serialize(),
        dataType: 'json',
        success: function (data){
            if (data.message === 'success'){
                $('#comments').load(document.URL +  ' #comments');
                $('#user-full-name').load(document.URL +  ' #user-full-name');
            }
        }

    })
}

