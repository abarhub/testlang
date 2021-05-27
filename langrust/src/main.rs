use std::env;

fn random_number(max: u32, last:&mut u64) -> u32
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

fn create_array(len:u32, max_value:u32,mut last:&mut u64)-> Vec<u32>
{
    let mut result1:Vec<u32> = Vec::new();
    for _i in 1..(len + 1) {
        result1.push(random_number(max_value,&mut last));
    }
    return result1;
}


fn main() {

    let mut tab_size:u32 = 10000000;
    let max_value:u32 = 5000000;
    let mut no_output = false;
    let mut debug = false;
    let mut last:u64=0;

    let args: Vec<String> = env::args().collect();

    for x in args.iter() {
        if x=="--nooutput"{
            no_output=true;
        } else if x.starts_with("--nbop=") {
            let s=&x[7..];
            let n: u32 = s
                .trim()
                .parse()
                .expect("Wanted a number");
            if n>0 {
                tab_size=n;
            }
        } else if x=="--debug" {
            debug = true;
        }
    }

    let mut vec=create_array(tab_size,max_value,&mut last);

    vec.sort();

    if debug {
        let mut i:u32=0;
        for x in args.iter()         {
            println!("   argv[{}] : '{}'\n", i,x);
            i=i+1;
        }
        println!("lang=rust;tabSize={};maxValue={};noOutput={};debug={}",
               tab_size, max_value, no_output, debug);
    }

    if !no_output{
        println!("Collected (0..10) into: {:?}",  &vec[..10]);
    }
}