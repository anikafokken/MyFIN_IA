document.addEventListener("DOMContentLoaded", function() {
    const typeField = document.querySelector('#id_account_type')
    const studentSelection = document.querySelector('#student-only-fields')
    const schoolSelection = document.querySelector('#school-fields')

    function toggleFields() {
        const account_type_value = typeField.value

        studentSelection.style.display = 'none';
        schoolSelection.style.display = 'none';

        // if (account_type_value == "STUDENT"):

        
    }
})