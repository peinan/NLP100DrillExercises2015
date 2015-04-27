//
//  03_pi.swift
//  
//
//  Created by Peinan ZHANG on 2015/04/27.
//
//

import Foundation

let str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
var words = split(str){$0 == " "}
for word in words {
    if word.hasSuffix(".") {
        word. // TODO: 他のswiftファイルの関数をimportできるかを調べる
    }
}