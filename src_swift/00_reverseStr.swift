//
//  00_reverseStr.swift
//  
//
//  Created by Peinan ZHANG on 2015/04/13.
//
//

var str = "stressed"
var strArray: [Character] = [Character]()
// make a str copy with Character Type
for character in str {
    strArray.append(character)
}
var reversedStr: String = ""
for var index = strArray.count - 1; index >= 0; --index {
    reversedStr.append(strArray[index])
}
println("\(str) -> \(reversedStr)")