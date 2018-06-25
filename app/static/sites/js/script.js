document.getElementById('addDivision').addEventListener('click', function (event) {
    $('#modalAddDivision').modal('show')
})

$('.delete-division').click( function() {
    $('#modalDeleteDivision').modal('show')
    var dataId = $(this).attr('data-id')
    var dataName = $(this).attr('data-name')
    document.getElementById('textDelete').innerHTML = 'Are you sure want to delete ' + dataName + ' division ?'
    var actionDeleteForm = document.getElementById('formDelete').getAttribute('action')
    document.getElementById('formDelete').setAttribute('action', actionDeleteForm.replace('0', dataId))
})

$('.detail-division').click( function () {
    var dataId = $(this).attr('data-id')

    axios.get('division/' + dataId).then(function (response) {
        document.getElementById('textDivisionName').innerText = response.data.name
        document.getElementById('textDivisionNote').innerText = response.data.note
    }).catch(function (error) {
        console.log(error)
    })

    $('#modalDetailDivision').modal('show')
})

$('.edit-division').click( function() {
    var dataId = $(this).attr('data-id')
    var actionDeleteForm = document.getElementById('formEdit').getAttribute('action')
    document.getElementById('formEdit').setAttribute('action', actionDeleteForm.replace('0', dataId))

    axios.get('division/' + dataId).then(function (response){
        var divisionName = document.getElementsByClassName('edit-division-name')
        var divisionNote = document.getElementsByClassName('edit-division-note')

        for (var i = 0; i < divisionName.length; i++) {
            var element = divisionName[i];
            element.setAttribute('value', response.data.name)
        }
        
        for (var j = 0; j < divisionNote.length; j++) {
            var element = divisionNote[j];
            element.setAttribute('value', response.data.note)
        }
        
    }).catch( function (error){
        console.log(error)
    })
    
    $('#modalEditDivision').modal('show')
})