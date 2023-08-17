<script>
    import {createEventDispatcher} from 'svelte';

    let inputPhoto
    let photoImg
    
    const dispatch = createEventDispatcher()
    
    const newPhoto = (e)=> { 
        let file = e.target.files[0]; 
        let reader = new FileReader();
        reader.readAsDataURL(file); 
            
        reader.onload = function(readerEvent) {
            let content = readerEvent.target.result; 
            photoImg.setAttribute('src', content);
        }

        dispatch(
            "photoLoaded", {}
        )
    };

    const selectPhoto= () =>{
        inputPhoto.click()
    }
</script>


<div  id="photoDiv" on:click={()=> selectPhoto()}>
    <input bind:this={inputPhoto} on:change={newPhoto} type="file" name="file" style="display: none;">
    <img bind:this={photoImg} class="photoImg" src="" alt="Elige una IMAGEN"/>
</div>

<style>
    .photoImg{
        border-radius: 45px;
        width: 200px;
        height: 200px;
        background-position: center;
        background-size: contain;
    }

    #photoDiv{
        border-radius: 45px;
        text-align: center;
        border:solid 1px;
        width: 200px;
        height: 200px;
        margin: 10px;
        cursor:pointer;
        background-position: center;
        background-size: contain;
    }
</style>
