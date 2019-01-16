async function f() {

    const delay = (duration) =>
        new Promise(resolve => setTimeout(resolve, duration))

  
    console.log('1')
    await delay(1000)
    console.log('2')
  }
  
  f();