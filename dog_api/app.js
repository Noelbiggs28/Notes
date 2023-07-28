async function fetchDog() {
    const dogURL = "https://dog.ceo/api/breeds/image/random"
    const response = await fetch(dogURL);
    const jsonData = await response.json();
    console.log(jsonData.message)
    const dog = document.querySelector('#dog')
    picture = dog.createElement('img')
    picture.href = jsonData.message
    dog.appendChild(picture)    
}









window.onload = () => {
    fetchDog()
    }