
/* 
// another way to declare : 
let nam = <string> "name";

// union variable  : which can be of more than one type
let surname:string|number;  //[either can be number or string]

// in case of function
const func = (n,  m) => {
    console.log(n, m)  // [here it is any]
}
const func1 = (n:any,  m:any) => {
    console.log(n, m)
}

const func2 = (n: number, m: number) : string =>{
    console.log(n, m);
    return n*m
}
*/

// type  and interface : they are functions
// and in react we'll see funtional components

type UserName = string | number ;  //type aliases
let a: UserName = "name";  //if you assign any other type [number and string then it will give error]



const fun = (n:number, m:number): number => {
    console.log(n, m);
    return n*m;
}

//similarly we can define alias for fun also to reduce its size