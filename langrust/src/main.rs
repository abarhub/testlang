

fn randomNumber(max: u32,mut last:&mut u64) -> u32
{
    let tmp2:u64=*last;
    let tmp01=(25214903917u128 * tmp2 as u128) as u64;
    let tmp03=(tmp01+ 11u64)%281474976710656u64;
    let tmp3:u64 =tmp03;
    *last= tmp3;
    let tmp:u64;
    tmp=*last;
    return (tmp % (max as u64)) as u32;
}

fn createArray(len:u32, maxValue:u32,mut last:&mut u64)-> Vec<u32>
{
    let mut result1:Vec<u32> = Vec::new();
    for i in 1..(len + 1) {
        result1.push(randomNumber(maxValue,&mut last));
    }
    return result1;
}


fn main() {

    let mut tabSize:u32 = 10000000;
    let maxValue:u32 = 5000000;
    let noOutput = false;
    let debug = false;
    let mut last:u64=0;

    tabSize=10;

    let mut a = [1,3,2];
    a.sort();
    println!("{:?}", a);

    let mut vec=createArray(tabSize,maxValue,&mut last);

    vec.sort();

    println!("Collected (0..10) into: {:?}", vec);
}