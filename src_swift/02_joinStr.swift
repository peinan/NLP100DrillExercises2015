//
//  02_joinStr.swift
//  
//
//  Created by Peinan ZHANG on 2015/04/27.
//
//

import Foundation

let str1 = "パトカー"
let str2 = "タクシー"
var chars1: [Character] = [Character]()
var chars2: [Character] = [Character]()

func convertToChars(str: String) -> [Character] {
    var chars: [Character] = [Character]()
    for aChar in str {
        chars.append(aChar)
    }
    return chars
}

chars1 = convertToChars(str1)
chars2 = convertToChars(str2)
var joinedStr: String = ""

for i in 0...chars1.count - 1 {
   joinedStr.append(chars1[i])
   joinedStr.append(chars2[i])
}

println("\(str1) + \(str2) -> \(joinedStr)")