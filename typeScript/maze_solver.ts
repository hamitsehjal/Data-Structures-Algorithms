function walk(maze:string[],wall:string,curr:Point,end:Point):boolean{
    // 1. Base Case
    // off the map
    if(curr.x<0||curr.x>=maze[0].length||
        curr.y<0||curr.y>=maze[0].length)
        {
            return false;
        }

    // on a wall
}

export default function solve(maze:string[],wall:string,start:Point, end:Point ):Point[]{

}