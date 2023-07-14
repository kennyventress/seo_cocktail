<script>
  document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('.list-group-item');

    links.forEach(function(link) {
      link.addEventListener('click', function(event) {
        event.preventDefault();
        const route = this.getAttribute('data-route');
        const url = "{{ url_for('') }}" + route;  // Replace '' with the appropriate Flask endpoint

        // Perform any desired actions or navigation with the generated URL
        // For example, you can use window.location.href to navigate to the URL
        window.location.href = url;
      });
    });
  });
</script>


{
  /* The following line can be included in your src/index.js or App.js file */
}
import 'bootstrap/dist/css/bootstrap.min.css';