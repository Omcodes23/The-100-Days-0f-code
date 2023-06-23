const addBtn=document.getElementById('addBtn');
const main=document.getElementById('main');

addBtn.addEventListener(
    "click",
    function(){
        addNote()
    }
)

function saveNotes(){
    const notes=document.querySelectorAll(".note textarea");
    const data=[]
    notes.forEach((note)=>{
        data.push(note.value)
    })
    localStorage.setItem('notes',JSON.stringify(data));
}

function addNote(text=""){
    const note=document.createElement("div");

    note.classList.add("note");
    note.innerHTML=`<div class="tool">
        <i class="save fas fa-save"></i>
        <i class="trash fas fa-trash"></i>
    </div>
    <textarea>${text}</textarea>`;
    
    note.querySelector(".save").addEventListener(
        "click",
        function(){
            saveNotes()
        }
    )

    note.querySelector(".trash").addEventListener(
        "click",
        function(){
            note.remove()
            saveNotes()
        }
    )

    note.querySelector("textarea").addEventListener(
        "focusout",
        function(){
            saveNotes()
        }
    )
    
    main.appendChild(note);
    saveNotes()
}

(
    function(){
        const lsNotes=JSON.parse(localStorage.getItem('notes'));
        if(lsNotes===null){
            addNote()
        }else{
            lsNotes.forEach((lsnote)=>{
                addNote(lsnote)
            })
        }
    }
)()