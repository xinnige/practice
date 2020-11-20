package main

import (
    "fmt"
    "golang.org/x/tour/tree"
)

// Walk walks the tree t sending all values
// from the tree to the channel ch.
func Walk(t *tree.Tree, ch chan int){
    walk(t, ch)
    close(ch)

}

func walk(t *tree.Tree, ch chan int){
    if t != nil {
        walk(t.Left, ch)
        ch <- t.Value
        walk(t.Right, ch)
    }
}

// Same determines whether the trees
// t1 and t2 contain the same values.
func Same(t1, t2 *tree.Tree) bool {
   ch1 := make(chan int)
   ch2 := make(chan int)

   go Walk(t1, ch1)
   go Walk(t2, ch2)

   for {
      n1, ok1 := <-ch1
      n2, ok2 := <-ch2
      if n1 != n2 || ok1 != ok2 {
        return false
      }
      if !ok1 {
        break
      }
   }
   return true
}

func main() {
    fmt.Printf("tree.New(1) = tree.New(1) %t \n", Same(tree.New(1), tree.New(1)))
    fmt.Printf("tree.New(1) = tree.New(2) %t \n", Same(tree.New(1), tree.New(2)))
    fmt.Printf("tree.New(2) = tree.New(2) %t \n", Same(tree.New(2), tree.New(2)))
    // go Walk(tree.New(1), ch)
    // for {
    //   select {
    //   case x, ok := <-ch:
    //      if !ok {
    //        fmt.Println()
    //        return
    //    }
    //    fmt.Printf("%d ", x)
    //   }
    // }
}

