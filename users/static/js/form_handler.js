document.addEventListener("DOMContentLoaded", function() {
    const typeField = document.querySelector('#account_type')
    const studentSelection = document.querySelector('#student-only-fields')
    const schoolSelection = document.querySelector('#school-fields')

    function toggleFields() {
        const account_type_value = typeField.value;
        console.log("Dropdown changed to: ", account_type_value);


        studentSelection.style.display = 'none';
        schoolSelection.style.display = 'none';

        if (account_type_value == "STUDENT") {
            console.log("Showing student section");
            studentSelection.style.display = 'block';
            schoolSelection.style.display = 'none';
        } else if (account_type_value == "SCHOOL") {
            console.log("Showing school section");
            schoolSelection.style.display = 'block';
            studentSelection.style.display = 'none';
        }


    }
    typeField.addEventListener('change', toggleFields)

    toggleFields();

})