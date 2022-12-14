/*
An AVL tree (Georgy Adelson-Velsky and Landis' tree, named after the inventors)
is a self-balancing binary search tree. In an AVL tree, the heights of the two
child subtrees of any node differ by at most one; if at any time they differ by
more than one, rebalancing is done to restore this property.
We define balance factor for each node as :
balanceFactor = height(left subtree) - height(right subtree)
The balance factor of any node of an AVL tree is in the integer range [-1,+1].
If after any modification in the tree, the balance factor becomes less than −1
or greater than +1, the subtree rooted at this node is unbalanced, and a
rotation is needed.
AVL_Tree_Rebalancing.svg.png
(https://en.wikipedia.org/wiki/AVL_tree)
You are given a pointer to the root of an AVL tree. You need to insert a value
into this tree and perform the necessary rotations to ensure that it remains
balanced.
Input Format
  You are given a function,
    node *insert(node * root,int new_val)
    {


    }
  'node' is defined as :
    struct node
    {
    int val;            //value
    struct node* left;  //left child
    struct node* right; //right child
    int ht;             //height of the node
    } node;
You only need to complete the function.
  Note: All the values in the tree will be distinct. Height of a Null node is -1
  and the height of the leaf node is 0.
Output Format
  Insert the new value into the tree and return a pointer to the root of the
  tree. Ensure that the tree remains balanced.
  Sample Input
      3
    /  \
   2    4
         \
          5
  The value to be inserted is 6.
Sample Output
      3
    /  \
   2    5
       / \
      4   6
Explanation
  After inserting 6 in the tree. the tree becomes:
      3 (Balance Factor = -2)
    /  \
   2    4 (Balance Factor = -2)
         \
          5 (Balance Factor = -1)
           \
            6 (Balance Factor = 0)
  Balance Factor of nodes 3 and 4 is no longer in the range [-1,1]. We need to
  perform a rotation to balance the tree. This is the right right case. We
  perform a single rotation to balance the tree.
  After performing the rotation, the tree becomes :
                                3 (Balance Factor = -1)
                              /   \
        (Balance Factor = 0) 2     5 (Balance Factor = 0)
                                  / \
             (Balance Factor = 0)4   6 (Balance Factor = 0)
*/


/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */


int ht(node * root){
    return (root == nullptr) ? -1 : root->ht;
}
struct unwind_escape{};
struct new_root{node* newroot{nullptr};};
struct impltag_t{} impltag;

node* left_rotate(node* parent){
    node* tmp = parent->right;
    parent->right = tmp->left;
    tmp->left = parent;
    parent->ht = (ht(parent->left) > ht(parent->right) ? ht(parent->left) : ht(parent->right))+1;
    tmp->ht = (ht(tmp->left) > ht(tmp->right) ? ht(tmp->left) : ht(tmp->right))+1;
    return tmp;
}
node* right_rotate(node* parent){
    node* tmp = parent->left;
    parent->left = tmp->right;
    tmp->right = parent;
    parent->ht = (ht(parent->left) > ht(parent->right) ? ht(parent->left) : ht(parent->right))+1;
    tmp->ht = (ht(tmp->left) > ht(tmp->right) ? ht(tmp->left) : ht(tmp->right))+1;
    return tmp;
}
void insert(impltag_t, node* parent, node * iter,int val){
    if(iter == nullptr) throw new_root{new node{val, nullptr, nullptr, 0}};
    if(val < iter->val){
        if(iter->left == nullptr){
            iter->left = new node{val, nullptr, nullptr, 0};
            iter->ht = 1;
            return;
        }
        else insert(impltag, iter, iter->left, val);
    }
    else{
        if(iter->right == nullptr){
            iter->right = new node{val, nullptr, nullptr, 0};
            iter->ht = 1;
            return;
        }
        else insert(impltag, iter, iter->right, val);
    }
    auto lht = ht(iter->left);
    auto rht = ht(iter->right);
    if(lht+1 > ht(iter) || rht+1 > ht(iter)){
        iter->ht = (lht > rht ? lht : rht) + 1;
        if(lht - rht > 1){
            if(ht(iter->left->left) - ht(iter->left->right) < 0){
                iter->left = left_rotate(iter->left);
            }
            (parent != nullptr ? parent->right == iter ?
             parent->right = right_rotate(iter) :
             parent->left = right_rotate(iter)  :
             throw new_root{right_rotate(iter)}
            );
        }
        else if(lht - rht < -1){
            if(ht(iter->right->left) - ht(iter->right->right) > 0){
                iter->right = right_rotate(iter->right);
            }
            (parent != nullptr ? parent->right == iter ?
             parent->right = left_rotate(iter) :
             parent->left = left_rotate(iter)  :
             throw new_root{left_rotate(iter)}
            );
        }
        return;
    }
    else throw unwind_escape{};
}
node * insert(node* root, int val){
    try{
        insert(impltag, nullptr, root, val);
    }
    catch(unwind_escape){}
    catch(new_root nr){
        return nr.newroot;
    }
    return root;
}
