document.addEventListener('DOMContentLoaded', function () {
    var var1 = document.getElementById('link-1')
    var var2 = document.getElementById('link-2')
    var var3 = document.getElementById('link-3')
    const contact = document.getElementById('contact')
    const btn1 = document.getElementById('btn-1')
    const btn2 = document.getElementById('btn-2')
    const btn3 = document.getElementById('btn-3')


    var1.addEventListener('click', () => {
        window.open("https://www.instagram.com/erfan_ethan/?hl=en")
    })
    var2.addEventListener('click', () => {
        window.open("https://www.linkedin.com/in/erfan-ezizi-4551a71a8/")
    })
    var3.addEventListener('click', () => {
        window.open("https://www.youtube.com/channel/UCdlF2wcuIjwaR6T2udOLDPQ?view_as=subscriber")
    })


    let searchForm = document.getElementById('searchForm');
    let pageLink = document.getElementsByClassName('page-link')

    for (var i = 0; pageLink.length > i; i++) {
        pageLink[i].addEventListener('click', (e) => {
            e.preventDefault()
            let page = this.dataset.page
            console.log('Page', page)
            searchForm.innerHTML += `<input value="${page}" name="page" hidden>`
            searchForm.submit()
        })
    }
    contact.addEventListener('click', () => {
        window.scroll(0, 1400)
    })
    btn1.addEventListener('click', () => {
        window.scroll(0, 400)
    })
    btn2.addEventListener('click', () => {
        window.scroll(0, 900)
    })
    btn3.addEventListener('click', () => {
        window.scroll(0, 1400)
    })

})




