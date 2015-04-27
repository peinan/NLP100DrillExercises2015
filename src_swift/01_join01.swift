//
//  01_join01.swift
//  
//
//  Created by Peinan ZHANG on 2015/04/13.
//
//

var str = "パタトクカシーー"
var strArray: [Character] = [Character]()
for aChar in str {
    strArray.append(aChar)
}
var extrStr: String = ""
let charPos = [0, 2, 4, 6]
for i in charPos {
    extrStr.append(strArray[i])
}
println("\(str) -> \(extrStr)")