document.addEventListener('DOMContentLoaded', function() {
    const missionButton = document.getElementById('mission-title');
    const missionStatement = document.getElementById('mission-statement');
    const formButton = document.getElementById('form-button');
    const formContainer = document.getElementById('form-container');
  
    missionButton.addEventListener('click', function() {
      if (missionStatement.classList.contains('show')) {
        missionStatement.classList.remove('show');
        missionStatement.style.maxHeight = null;
      } else {
        missionStatement.classList.add('show');
        missionStatement.style.maxHeight = missionStatement.scrollHeight + 'px';
      }
    });
  
    formButton.addEventListener('click', function() {
      if (formContainer.style.display === 'none') {
        formContainer.style.display = 'block';
      } else {
        formContainer.style.display = 'none';
      }
    });
  });